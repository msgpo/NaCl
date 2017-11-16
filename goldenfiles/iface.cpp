#include <iostream>
#include <net/inet4>
#include <net/ip4/cidr.hpp>
#include <plugins/nacl.hpp>
#include <net/nat/napt.hpp>
#include <net/vlan>

using namespace net;

std::shared_ptr<Conntrack> nacl_ct_obj;
std::unique_ptr<nat::NAPT> nacl_natty_obj;

namespace custom_made_classes_from_nacl {

class My_Filter : public nacl::Filter {
public:
	Filter_verdict operator()(IP4::IP_packet& pckt, Inet<IP4>& stack, Conntrack::Entry_ptr ct_entry) {
		if (not ct_entry) {
return Filter_verdict::DROP;
}
return Filter_verdict::ACCEPT;

	}
};

} //< namespace custom_made_classes_from_nacl

void register_plugin_nacl() {
	INFO("NaCl", "Registering NaCl plugin");

	auto& eth1 = Inet4::stack<1>();
	Inet4::ifconfig<1>(10.0, [&eth1] (bool timedout) {
		if (timedout) {
			INFO("NaCl plugin interface eth1", "DHCP timeout (%s) - falling back to static configuration", eth1.ifname().c_str());
			eth1.network_config(IP4::addr{10,0,0,50}, IP4::addr{255,255,255,0}, IP4::addr{10,0,0,1}, IP4::addr{8,8,8,8});
		}
	});
	auto& eth0 = Inet4::stack<0>();
	eth0.network_config(IP4::addr{10,0,0,45}, IP4::addr{255,255,255,0}, IP4::addr{10,0,0,1}, IP4::addr{8,8,8,8});

	// For each iface:
	auto& eth1_nic = eth1.nic();
	auto& eth1_manager = VLAN_manager::get(1);
	// For each vlan connected to this iface:
	Super_stack::inet().create<IP4>(eth1_manager.add(eth1_nic, 0), 1, 0).network_config(IP4::addr{10,10,10,10}, IP4::addr{255,255,255,0}, IP4::addr{10,0,0,1});
	Super_stack::inet().create<IP4>(eth1_manager.add(eth1_nic, 1), 1, 1).network_config(IP4::addr{10,20,10,10}, IP4::addr{255,255,255,0}, IP4::addr{10,0,0,1});

	// For each iface:
	auto& eth0_nic = eth0.nic();
	auto& eth0_manager = VLAN_manager::get(0);
	// For each vlan connected to this iface:
	Super_stack::inet().create<IP4>(eth0_manager.add(eth0_nic, 0), 0, 0).network_config(IP4::addr{10,10,10,10}, IP4::addr{255,255,255,0}, IP4::addr{10,0,0,1});

	custom_made_classes_from_nacl::My_Filter my_filter;

	eth1.ip_obj().input_chain().chain.push_back(my_filter);

	eth1.ip_obj().postrouting_chain().chain.push_back(my_filter);

	eth1.ip_obj().prerouting_chain().chain.push_back(my_filter);

	eth1.ip_obj().output_chain().chain.push_back(my_filter);

	eth0.ip_obj().prerouting_chain().chain.push_back(my_filter);

	eth0.ip_obj().input_chain().chain.push_back(my_filter);

	eth0.ip_obj().output_chain().chain.push_back(my_filter);

	eth0.ip_obj().postrouting_chain().chain.push_back(my_filter);

	// Ct

	nacl_ct_obj = std::make_shared<Conntrack>();

	INFO("NaCl", "Enabling Conntrack on eth1");
	eth1.enable_conntrack(nacl_ct_obj);

	INFO("NaCl", "Enabling Conntrack on eth0");
	eth0.enable_conntrack(nacl_ct_obj);

	// NAT

	nacl_natty_obj = std::make_unique<nat::NAPT>(nacl_ct_obj);

	auto masq = [](IP4::IP_packet& pckt, Inet<IP4>& stack, Conntrack::Entry_ptr entry)->auto {
		nacl_natty_obj->masquerade(pckt, stack, entry);
		return Filter_verdict::ACCEPT;
	};
	auto demasq = [](IP4::IP_packet& pckt, Inet<IP4>& stack, Conntrack::Entry_ptr entry)->auto {
		nacl_natty_obj->demasquerade(pckt, stack, entry);
		return Filter_verdict::ACCEPT;
	};

	INFO("NaCl", "Enable MASQUERADE on eth1");
	eth1.ip_obj().prerouting_chain().chain.push_back(demasq);
	eth1.ip_obj().postrouting_chain().chain.push_back(masq);

	INFO("NaCl", "Enable MASQUERADE on eth0");
	eth0.ip_obj().prerouting_chain().chain.push_back(demasq);
	eth0.ip_obj().postrouting_chain().chain.push_back(masq);
}