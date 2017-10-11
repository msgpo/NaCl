import sys

# Languages that NaCl can be transpiled to

CPP = "cpp"

valid_languages = [
	CPP
]

# Operators

GREATER_THAN_OR_EQUAL 	= ">="
LESS_THAN_OR_EQUAL 		= "<="
GREATER_THAN 			= ">"
LESS_THAN 				= "<"
EQUALS 					= "=="
NOT_EQUALS 				= "!="

NOT = "!"

IN = "in"

AND = "and"
OR 	= "or"

ARROW 	= "->"
DOT 	= "."

PARENTHESIS_START 	= "("
PARENTHESIS_END 	= ")"

# Other

MASK_LIMIT = 32
BYTE_LIMIT = 255

IS_LIST = True

TRUE 	= "true"
FALSE 	= "false"

# Possible NaCl types
TYPE_IFACE 		= "iface"
TYPE_VLAN 		= "vlan"
TYPE_GATEWAY 	= "gateway"
TYPE_FILTER 	= "filter"
TYPE_REWRITE 	= "rewrite"
TYPE_NAT 		= "nat"

valid_nacl_types = [
	TYPE_IFACE,
	TYPE_VLAN,
	TYPE_GATEWAY,
	TYPE_FILTER,
	TYPE_REWRITE,
	TYPE_NAT
]

BASE_TYPE_FUNCTION 		= "function"
BASE_TYPE_UNTYPED_INIT 	= "untyped_init"
BASE_TYPE_TYPED_INIT 	= "typed_init"

# ---- Iface keys ----

IFACE_KEY_ADDRESS 		= "address"
IFACE_KEY_NETMASK 		= "netmask"
IFACE_KEY_GATEWAY		= "gateway"
IFACE_KEY_DNS 			= "dns"
IFACE_KEY_INDEX 		= "index"
IFACE_KEY_VLAN 			= "vlan"
IFACE_KEY_MASQUERADE 	= "masquerade"
IFACE_KEY_CONFIG 		= "config"

IFACE_KEY_PREROUTING 	= "prerouting"
IFACE_KEY_INPUT 		= "input"
IFACE_KEY_FORWARD 		= "forward"
IFACE_KEY_OUTPUT 		= "output"
IFACE_KEY_POSTROUTING 	= "postrouting"

chains = [
	IFACE_KEY_PREROUTING,
	IFACE_KEY_INPUT,
	IFACE_KEY_FORWARD,
	IFACE_KEY_OUTPUT,
	IFACE_KEY_POSTROUTING
]

predefined_iface_keys = [
	IFACE_KEY_ADDRESS,
	IFACE_KEY_NETMASK,
	IFACE_KEY_GATEWAY,
	IFACE_KEY_DNS,
	IFACE_KEY_INDEX,
	IFACE_KEY_VLAN,
	IFACE_KEY_MASQUERADE,
	IFACE_KEY_CONFIG
]
predefined_iface_keys.extend(chains)

DHCP_CONFIG 			= "dhcp"
DHCP_FALLBACK_CONFIG 	= "dhcp-with-fallback"
STATIC_CONFIG 			= "static"

predefined_config_types = [
	DHCP_CONFIG,
	DHCP_FALLBACK_CONFIG,
	STATIC_CONFIG
]

VLAN_KEY_ADDRESS 	= IFACE_KEY_ADDRESS
VLAN_KEY_NETMASK 	= IFACE_KEY_NETMASK
VLAN_KEY_GATEWAY 	= IFACE_KEY_GATEWAY
VLAN_KEY_DNS 		= IFACE_KEY_DNS
VLAN_KEY_INDEX 		= IFACE_KEY_INDEX

predefined_vlan_keys = [
	VLAN_KEY_ADDRESS,
	VLAN_KEY_NETMASK,
	VLAN_KEY_GATEWAY,
	VLAN_KEY_INDEX
]

GATEWAY_KEY_HOST 	= "host"
GATEWAY_KEY_NET 	= "net"
GATEWAY_KEY_NETMASK = "netmask"
GATEWAY_KEY_NEXTHOP = "nexthop"
GATEWAY_KEY_IFACE 	= "iface"
GATEWAY_KEY_COST 	= "cost"

predefined_gateway_keys = [
	GATEWAY_KEY_HOST,
	GATEWAY_KEY_NET,
	GATEWAY_KEY_NETMASK,
	GATEWAY_KEY_NEXTHOP,
	GATEWAY_KEY_IFACE,
	GATEWAY_KEY_COST
]

AUTO = "auto"

TCP 	= "tcp"
UDP 	= "udp"
IP 		= "ip"
ICMP 	= "icmp"
CT 		= "ct"

NAT_OBJ_NAME 	= "natty"

# Pckt variable names, used in transpiled text/code
TCP_PCKT 		= "tcp_pckt"
UDP_PCKT 		= "udp_pckt"
IP_PCKT 		= "pckt"
ICMP_PCKT 		= "icmp_pckt"

pckt_names = {
	TCP: 	TCP_PCKT,
	UDP: 	UDP_PCKT,
	IP: 	IP_PCKT,
	ICMP: 	ICMP_PCKT
}

# IncludeOS packet classes
INCLUDEOS_TCP_PCKT_CLASS 	= "tcp::Packet"
INCLUDEOS_UDP_PCKT_CLASS 	= "PacketUDP"
INCLUDEOS_ICMP_PCKT_CLASS 	= "icmp4::Packet"
INCLUDEOS_IP_PCKT_CLASS 	= "IP4::IP_packet"

cpp_pckt_classes = {
	TCP: 	INCLUDEOS_TCP_PCKT_CLASS,
	UDP: 	INCLUDEOS_UDP_PCKT_CLASS,
	ICMP: 	INCLUDEOS_ICMP_PCKT_CLASS,
	IP: 	INCLUDEOS_IP_PCKT_CLASS
}

INCLUDEOS_REFERENCE_OP = "&"

# IncludeOS class names
INCLUDEOS_IP4_ADDR_CLASS = "IP4::addr"
INCLUDEOS_IP4_CIDR_CLASS = "ip4::Cidr"

# NaCl verdicts/actions
ACCEPT 	= 'accept'
DROP 	= 'drop'
LOG 	= 'log'
SNAT 	= 'snat'
DNAT 	= 'dnat'

MASQUERADE = "masquerade"

# IncludeOS (C++) Filter return values
INCLUDEOS_FILTER_VERDICT_NS 	= "Filter_verdict::"
INCLUDEOS_DROP 					= "return " + INCLUDEOS_FILTER_VERDICT_NS + "DROP;\n"
INCLUDEOS_ACCEPT 				= "return " + INCLUDEOS_FILTER_VERDICT_NS + "ACCEPT;\n"

INCLUDEOS_CT_ENTRY = "ct_entry"

SSH 	= "ssh"
DNS 	= "dns"
HTTP 	= "http"
HTTPS 	= "https"

# TCP, UDP and IP packet properties (NaCl)

SPORT 		= "sport"
DPORT 		= "dport"
SEQUENCE 	= "sequence"
ACKSEQ 		= "ackseq"
DOFF 		= "doff"
RESERVED 	= "reserved"
FLAGS 		= "flags"
WINDOW 		= "window"
CHECKSUM 	= "checksum"
URGPTR 		= "urgptr"
LENGTH 		= "length"

VERSION 	= "version"
HDRLENGTH 	= "hdrlength"
DSCP 		= "dscp"
ECN 		= "ecn"
ID 			= "id"
FRAG_OFF 	= "frag-off"
TTL 		= "ttl"
PROTOCOL 	= "protocol"
SADDR 		= "saddr"
DADDR 		= "daddr"

# TCP, UDP and IP packet properties/methods in IncludeOS (C++)

INCLUDEOS_SPORT = "src_port()"
INCLUDEOS_DPORT = "dst_port()"

INCLUDEOS_TCP_SEQUENCE 	= "seq()"
INCLUDEOS_TCP_ACKSEQ 	= "ack()"
INCLUDEOS_TCP_DOFF 		= "offset()"
INCLUDEOS_TCP_RESERVED 	= "tcp_header().offset_flags.offset_reserved"
INCLUDEOS_TCP_FLAGS 	= "tcp_header().offset_flags.flags"
INCLUDEOS_TCP_WINDOW 	= "win()"
INCLUDEOS_TCP_CHECKSUM 	= "tcp_checksum()"
INCLUDEOS_TCP_URGPTR 	= "tcp_header().urgent"

INCLUDEOS_UDP_CHECKSUM 	= "checksum()"
INCLUDEOS_UDP_LENGTH 	= "length()"

INCLUDEOS_IP_VERSION 	= "ip_version()"
INCLUDEOS_IP_HDRLENGTH 	= "ip_header_length()"
INCLUDEOS_IP_DSCP 		= "ip_dscp()"
INCLUDEOS_IP_ECN 		= "ip_ecn()"
INCLUDEOS_IP_LENGTH 	= "ip_total_length()"
INCLUDEOS_IP_ID 		= "ip_id()"
INCLUDEOS_IP_FRAG_OFF 	= "ip_frag_offs()"
INCLUDEOS_IP_TTL 		= "ip_ttl()"
INCLUDEOS_IP_PROTOCOL 	= "ip_protocol()"
INCLUDEOS_IP_CHECKSUM 	= "ip_checksum()"
INCLUDEOS_IP_SADDR 		= "ip_src()"
INCLUDEOS_IP_DADDR 		= "ip_dst()"

# ICMP and CT properties (NaCl)

TYPE 	= "type"
STATE 	= "state"

# ICMP and CT properties/methods in IncludeOS (C++)

INCLUDEOS_ICMP_TYPE = "type()"
INCLUDEOS_CT_STATE 	= "state"

# Protocols in IncludeOS (C++)

INCLUDEOS_PROTO_TCP 	= "Protocol::TCP"
INCLUDEOS_PROTO_UDP 	= "Protocol::UDP"
INCLUDEOS_PROTO_ICMP 	= "Protocol::ICMPv4"
INCLUDEOS_PROTO_IP4		= "Protocol::IPv4"
# INCLUDEOS_PROTO_IP6 	= "Protocol::IPv6"

# IncludeOS ICMP packet method to access IP part of packet

INCLUDEOS_ICMP_IP_ACCESS_METHOD = "ip()"

# ICMP types (NaCl)

ECHO_REPLY 			= "echo-reply"
DEST_UNREACHABLE 	= "destination-unreachable"
REDIRECT 			= "redirect"
ECHO_REQUEST 		= "echo-request"
TIME_EXCEEDED 		= "time-exceeded"
PARAMETER_PROBLEM 	= "parameter-problem"
TIMESTAMP_REQUEST 	= "timestamp-request"
TIMESTAMP_REPLY 	= "timestamp-reply"

# ICMP types in IncludeOS (C++)

ICMP_TYPE_NS = "icmp4::Type::"
INCLUDEOS_TYPE_ECHO_REPLY 			= ICMP_TYPE_NS + "ECHO_REPLY"
INCLUDEOS_TYPE_DEST_UNREACHABLE 	= ICMP_TYPE_NS + "DEST_UNREACHABLE"
INCLUDEOS_TYPE_REDIRECT 			= ICMP_TYPE_NS + "REDIRECT"
INCLUDEOS_TYPE_ECHO_REQUEST 		= ICMP_TYPE_NS + "ECHO"
INCLUDEOS_TYPE_TIME_EXCEEDED		= ICMP_TYPE_NS + "TIME_EXCEEDED"
INCLUDEOS_TYPE_PARAMETER_PROBLEM 	= ICMP_TYPE_NS + "PARAMETER_PROBLEM"
INCLUDEOS_TYPE_TIMESTAMP_REQUEST 	= ICMP_TYPE_NS + "TIMESTAMP"
INCLUDEOS_TYPE_TIMESTAMP_REPLY 		= ICMP_TYPE_NS + "TIMESTAMP_REPLY"

# CT states (NaCl)

ESTABLISHED = "established"
NEW 		= "new"
RELATED 	= "related"
INVALID 	= "invalid"

# CT states in IncludeOS (C++)

CT_STATE_NS = "Conntrack::State::"
INCLUDEOS_STATE_ESTABLISHED	= CT_STATE_NS + "ESTABLISHED"
INCLUDEOS_STATE_NEW 		= CT_STATE_NS + "NEW"
INCLUDEOS_STATE_RELATED 	= CT_STATE_NS + "RELATED"
INCLUDEOS_STATE_INVALID 	= CT_STATE_NS + "INVALID"

INCLUDEOS_CT_ENTRY_NULLPTR_CHECK = "if (not " + INCLUDEOS_CT_ENTRY + ") {\n" + INCLUDEOS_DROP + "}\n"

# TCP flags (NaCl)

FIN = "fin"
SYN = "syn"
RST = "rst"
PSH = "psh"
ACK = "ack"
URG = "urg"
CWR = "cwr"
# Also available in IncludeOS:
ECE = "ece"
NS 	= "ns"

# TCP flags in IncludeOS (C++)

TCP_FLAG_NS = "tcp::Flag::"
INCLUDEOS_FLAG_FIN 	= TCP_FLAG_NS + "FIN"
INCLUDEOS_FLAG_SYN 	= TCP_FLAG_NS + "SYN"
INCLUDEOS_FLAG_RST 	= TCP_FLAG_NS + "RST"
INCLUDEOS_FLAG_PSH 	= TCP_FLAG_NS + "PSH"
INCLUDEOS_FLAG_ACK 	= TCP_FLAG_NS + "ACK"
INCLUDEOS_FLAG_URG 	= TCP_FLAG_NS + "URG"
INCLUDEOS_FLAG_CWR 	= TCP_FLAG_NS + "CWR"
INCLUDEOS_FLAG_ECE 	= TCP_FLAG_NS + "ECE"
INCLUDEOS_FLAG_NS 	= TCP_FLAG_NS + "NS"

# All elements (Iface, Filter, Port, etc.) that have been identified in the NaCl file
# (by the visitor) are placed here because each language template (f.ex. cpp_template.py)
# needs to access the elements when resolving a variable name f.ex.
# Dictionary where key is the name of the Element and the value is the Element object or
# subtype of this
elements = {}

# Available/legal object types for given subtypes (tcp, udp, icmp, ip)
legal_obj_types = {
	TCP: 	[TCP, IP, CT],
	UDP: 	[UDP, IP, CT],
	ICMP: 	[ICMP, IP, CT],
	IP: 	[IP, CT]
}

legal_nested_subtypes = {
	TCP:	[IP, TCP],
	UDP:	[IP, UDP],
	ICMP: 	[IP, ICMP],
	IP: 	[IP, TCP, UDP, ICMP]
}

# TODO
# To be implemented in IncludeOS:

OIF 	= "oif"
OIFNAME = "oifname"
IIF 	= "iif"
IIFNAME = "iifname"

INCLUDEOS_OIF 		= "stack2.oif()"
INCLUDEOS_OIFNAME 	= "stack2.oifname()"
INCLUDEOS_IIF 		= "stack.iif()"
INCLUDEOS_IIFNAME 	= "stack.iifname()"

# Built-in/predefined constants that can be used as values in NaCl
predefined_values_cpp = {

	OIF:		INCLUDEOS_OIF,
	OIFNAME:	INCLUDEOS_OIFNAME,
	IIF:		INCLUDEOS_IIF,
	IIFNAME:	INCLUDEOS_IIFNAME,

	# TCP flags
	
	FIN: 	INCLUDEOS_FLAG_FIN,
	SYN: 	INCLUDEOS_FLAG_SYN,
	RST: 	INCLUDEOS_FLAG_RST,
	PSH: 	INCLUDEOS_FLAG_PSH,
	ACK: 	INCLUDEOS_FLAG_ACK,
	URG: 	INCLUDEOS_FLAG_URG,
	CWR: 	INCLUDEOS_FLAG_CWR,
	# Also available in IncludeOS:
	ECE:	INCLUDEOS_FLAG_ECE,
	NS: 	INCLUDEOS_FLAG_NS,

	# Named ports

	SSH: 	22,
	DNS: 	53,
	HTTP: 	80,
	HTTPS: 	443,

	# IP protocols
	
	TCP: 	INCLUDEOS_PROTO_TCP,
	UDP: 	INCLUDEOS_PROTO_UDP,
	ICMP: 	INCLUDEOS_PROTO_ICMP,
	IP: 	INCLUDEOS_PROTO_IP4,

	# ICMP types

	ECHO_REPLY: 		INCLUDEOS_TYPE_ECHO_REPLY,
	DEST_UNREACHABLE: 	INCLUDEOS_TYPE_DEST_UNREACHABLE,
	REDIRECT: 			INCLUDEOS_TYPE_REDIRECT,
	ECHO_REQUEST: 		INCLUDEOS_TYPE_ECHO_REQUEST,
	TIME_EXCEEDED: 		INCLUDEOS_TYPE_TIME_EXCEEDED,
	PARAMETER_PROBLEM: 	INCLUDEOS_TYPE_PARAMETER_PROBLEM,
	TIMESTAMP_REQUEST: 	INCLUDEOS_TYPE_TIMESTAMP_REQUEST,
	TIMESTAMP_REPLY: 	INCLUDEOS_TYPE_TIMESTAMP_REPLY,

	# CT states
	
	ESTABLISHED: 	INCLUDEOS_STATE_ESTABLISHED,
	NEW: 			INCLUDEOS_STATE_NEW,
	RELATED: 		INCLUDEOS_STATE_RELATED,
	INVALID: 		INCLUDEOS_STATE_INVALID
}

class Tcp:
	def __init__(self):
		self.properties = [
			SPORT,
			DPORT,
			SEQUENCE,
			ACKSEQ,
			DOFF,
			RESERVED,
			FLAGS,
			WINDOW,
			CHECKSUM,
			URGPTR
		]

		self.cpp_properties = {
			SPORT: 		INCLUDEOS_SPORT,
			DPORT: 		INCLUDEOS_DPORT,
			SEQUENCE: 	INCLUDEOS_TCP_SEQUENCE,
			ACKSEQ:		INCLUDEOS_TCP_ACKSEQ,
			DOFF: 		INCLUDEOS_TCP_DOFF,
			RESERVED: 	INCLUDEOS_TCP_RESERVED,
			FLAGS: 		INCLUDEOS_TCP_FLAGS,
			WINDOW: 	INCLUDEOS_TCP_WINDOW,
			CHECKSUM: 	INCLUDEOS_TCP_CHECKSUM,
			URGPTR: 	INCLUDEOS_TCP_URGPTR
		}

	def resolve_cast(self, language, prop):
		if language == CPP:
			return self.resolve_cast_cpp(prop)

	def resolve_method(self, language, prop):
		if language == CPP:
			return self.resolve_method_cpp(prop)

	def resolve_cast_cpp(self, prop):
		return ""

	def resolve_method_cpp(self, prop):
		if prop not in self.properties:
			sys.exit("Error: No property named " + prop + " in TCP")
		return self.cpp_properties[prop]

class Udp:
	def __init__(self):
		self.properties = [
			SPORT,
			DPORT,
			LENGTH,
			CHECKSUM
		]

		self.cpp_properties = {
			SPORT: 		INCLUDEOS_SPORT,
			DPORT: 		INCLUDEOS_DPORT,
			LENGTH: 	INCLUDEOS_UDP_LENGTH,
			CHECKSUM: 	INCLUDEOS_UDP_CHECKSUM
		}

	def resolve_cast(self, language, prop):
		if language == CPP:
			return self.resolve_cast_cpp(prop)

	def resolve_method(self, language, prop):
		if language == CPP:
			return self.resolve_method_cpp(prop)

	def resolve_cast_cpp(self, prop):
		return ""

	def resolve_method_cpp(self, prop):
		if prop not in self.properties:
			sys.exit("Error: No property named " + prop + " in UDP")
		return self.cpp_properties[prop]

class Ip:
	def __init__(self):
		self.properties = [
			VERSION,
			HDRLENGTH,
			DSCP,
			ECN,
			LENGTH,
			ID,
			FRAG_OFF,
			TTL,
			PROTOCOL,
			CHECKSUM,
			SADDR,
			DADDR
		]

		self.cpp_properties = {
			VERSION: 	INCLUDEOS_IP_VERSION,
			HDRLENGTH:	INCLUDEOS_IP_HDRLENGTH,
			DSCP: 		INCLUDEOS_IP_DSCP,
			ECN: 		INCLUDEOS_IP_ECN,
			LENGTH: 	INCLUDEOS_IP_LENGTH,
			ID: 		INCLUDEOS_IP_ID,
			FRAG_OFF: 	INCLUDEOS_IP_FRAG_OFF,
			TTL: 		INCLUDEOS_IP_TTL,
			PROTOCOL: 	INCLUDEOS_IP_PROTOCOL,
			CHECKSUM: 	INCLUDEOS_IP_CHECKSUM,
			SADDR: 		INCLUDEOS_IP_SADDR,
			DADDR: 		INCLUDEOS_IP_DADDR
		}

		# ?
		self.cpp_protocols = {
			TCP: 	INCLUDEOS_PROTO_TCP,
			UDP:	INCLUDEOS_PROTO_UDP,
			ICMP: 	INCLUDEOS_PROTO_ICMP,
			IP: 	INCLUDEOS_PROTO_IP4
		}

	def resolve_cast(self, language, prop):
		if language == CPP:
			return self.resolve_cast_cpp(prop)

	def resolve_method(self, language, prop):
		if language == CPP:
			return self.resolve_method_cpp(prop)

	def resolve_protocol(self, language, nacl_proto):
		if language == CPP:
			return self.resolve_protocol_cpp(nacl_proto)

	def resolve_cast_cpp(self, prop):
		if prop != DSCP and prop != ECN:
			return ""
		return "(uint8_t)"

	def resolve_method_cpp(self, prop):
		if prop not in self.properties:
			sys.exit("Error: No property named " + prop + " in IP")
		return self.cpp_properties[prop]

	# Returns the correct C++/IncludeOS IP protocol constant based on the
	# incoming (NaCl) protocol (tcp, udp, icmp)
	def resolve_protocol_cpp(self, nacl_proto):
		proto = nacl_proto.lower()
		if proto not in self.cpp_protocols:
			sys.exit("Error: No protocol named " + nacl_proto + " exists")
		return self.cpp_protocols[proto]

class Icmp:
	def __init__(self):
		self.properties = [
			TYPE
		]

		self.cpp_properties = {
			TYPE: INCLUDEOS_ICMP_TYPE
		}

	def resolve_cast(self, language, prop):
		if language == CPP:
			return self.resolve_cast_cpp(prop)

	def resolve_method(self, language, prop):
		if language == CPP:
			return self.resolve_method_cpp(prop)

	def resolve_cast_cpp(self, prop):
		return ""

	def resolve_method_cpp(self, prop):
		if prop not in self.properties:
			sys.exit("Error: No property named " + prop + " in ICMP")
		return self.cpp_properties[prop]

class Ct:
	def __init__(self):
		self.properties = [
			STATE
		]

		self.cpp_properties = {
			STATE: INCLUDEOS_CT_STATE
		}

	def resolve_cast(self, language, prop):
		if language == CPP:
			return self.resolve_cast_cpp(prop)

	def resolve_method(self, language, prop):
		if language == CPP:
			return self.resolve_method_cpp(prop)

	def resolve_cast_cpp(self, prop):
		return ""

	def resolve_method_cpp(self, prop):
		if prop not in self.properties:
			sys.exit("Error: No property named " + prop + " in CT")
		return self.cpp_properties[prop]

Tcp_obj = Tcp()
Udp_obj = Udp()
Ip_obj = Ip()
Icmp_obj = Icmp()
Ct_obj = Ct()

proto_objects = {
	TCP: 	Tcp_obj,
	UDP: 	Udp_obj,
	IP: 	Ip_obj,
	ICMP: 	Icmp_obj,
	CT: 	Ct_obj
}