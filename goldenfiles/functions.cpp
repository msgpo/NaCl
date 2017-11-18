#include <iostream>
#include <net/inet4>
#include <net/ip4/cidr.hpp>
#include <plugins/nacl.hpp>

using namespace net;

std::shared_ptr<Conntrack> nacl_ct_obj;

namespace custom_made_classes_from_nacl {

class My_Ip_Filter : public nacl::Filter {
public:
	Filter_verdict<IP4> operator()(IP4::IP_packet_ptr pckt, Inet<IP4>& stack, Conntrack::Entry_ptr ct_entry) {
		if (not ct_entry) {
return {nullptr, Filter_verdict_type::DROP};
}
if (ct_entry->state == Conntrack::State::ESTABLISHED) {
return {std::move(pckt), Filter_verdict_type::ACCEPT};
}
if (pckt->ip_protocol() == Protocol::ICMPv4) {
std::cout << "ICMP protocol\n";
}
if (pckt->ip_protocol() == Protocol::UDP) {
std::cout << "UDP protocol\n";
}
if (pckt->ip_protocol() == Protocol::TCP) {
std::cout << "TCP protocol\n";
}
if (pckt->ip_protocol() == Protocol::ICMPv4) {
auto icmp_pckt = icmp4::Packet(std::move(pckt));

std::cout << "1 ICMP filter reached\n";
if (icmp_pckt.type() == icmp4::Type::ECHO) {
std::cout << "1 ICMP: type == echo-request\n";
}
if (icmp_pckt.type() == icmp4::Type::ECHO_REPLY) {
std::cout << "1 ICMP: type == echo-reply\n";
}
if (icmp_pckt.ip().ip_src() != IP4::addr{10,0,0,45}) {
std::cout << "1 ICMP: IP saddr != 10.0.0.45\n";
}
std::cout << "1 ICMP: IP Filter inside ICMP Filter reached\n";
if (icmp_pckt.ip().ip_dst() != IP4::addr{10,0,0,45}) {
std::cout << "1 ICMP: IP daddr != 10.0.0.45\n";
}
pckt = icmp_pckt.release();
}
if (pckt->ip_protocol() == Protocol::UDP) {
auto& udp_pckt = static_cast<PacketUDP&>(*pckt);

std::cout << "1 UDP filter reached\n";
if (udp_pckt.src_port() != 100) {
std::cout << "1 UDP: sport != 100\n";
}
if (udp_pckt.ip_src() != IP4::addr{10,0,0,100}) {
std::cout << "1 UDP: IP saddr != 10.0.0.100\n";
}
std::cout << "1 UDP: IP Filter inside UDP Filter reached\n";
if (udp_pckt.ip_dst() != IP4::addr{10,0,0,45}) {
std::cout << "1 UDP: IP daddr != 10.0.0.45\n";
}
}
if (pckt->ip_protocol() == Protocol::TCP) {
auto& tcp_pckt = static_cast<tcp::Packet&>(*pckt);

std::cout << "1 TCP filter reached\n";
if (tcp_pckt.src_port() != 10) {
std::cout << "1 TCP: sport != 10\n";
}
if (tcp_pckt.ip_src() != IP4::addr{10,0,0,100}) {
std::cout << "1 TCP: IP saddr != 10.0.0.100\n";
}
std::cout << "1 TCP: IP Filter inside TCP Filter reached\n";
if (tcp_pckt.ip_dst() != IP4::addr{10,0,0,45}) {
std::cout << "1 TCP: IP daddr != 10.0.0.45\n";
}
}
if (pckt->ip_protocol() == Protocol::ICMPv4) {
auto icmp_pckt = icmp4::Packet(std::move(pckt));

std::cout << "2 ICMP filter reached\n";
if (icmp_pckt.type() != icmp4::Type::DEST_UNREACHABLE) {
std::cout << "2 ICMP: type != destination-unreachable\n";
}
if (icmp_pckt.ip().ip_src() != IP4::addr{10,0,0,60}) {
std::cout << "2 ICMP: IP saddr != 10.0.0.60\n";
}
pckt = icmp_pckt.release();
}
if (pckt->ip_protocol() == Protocol::UDP) {
auto& udp_pckt = static_cast<PacketUDP&>(*pckt);

std::cout << "2 UDP filter reached\n";
if (udp_pckt.checksum() > 10) {
std::cout << "2 UDP: checksum > 10\n";
}
if (udp_pckt.ip_checksum() > 10) {
std::cout << "2 UDP: IP checksum > 10\n";
}
}
if (pckt->ip_protocol() == Protocol::TCP) {
auto& tcp_pckt = static_cast<tcp::Packet&>(*pckt);

std::cout << "2 TCP filter reached\n";
if (tcp_pckt.dst_port() != 10) {
std::cout << "2 TCP: dport != 10\n";
}
if (tcp_pckt.ip_dst() != IP4::addr{10,0,0,10}) {
std::cout << "2 TCP: IP daddr != 10.0.0.10\n";
}
}
std::cout << "Default verdict: Accepting\n";
return {std::move(pckt), Filter_verdict_type::ACCEPT};

	}
};

} //< namespace custom_made_classes_from_nacl

void register_plugin_nacl() {
	INFO("NaCl", "Registering NaCl plugin");

	auto& eth0 = Inet4::stack<0>();
	eth0.network_config(IP4::addr{10,0,0,50}, IP4::addr{255,255,255,0}, IP4::addr{10,0,0,1});

	custom_made_classes_from_nacl::My_Ip_Filter my_ip_filter;

	eth0.ip_obj().input_chain().chain.push_back(my_ip_filter);

	// Ct

	nacl_ct_obj = std::make_shared<Conntrack>();

	INFO("NaCl", "Enabling Conntrack on eth0");
	eth0.enable_conntrack(nacl_ct_obj);
}