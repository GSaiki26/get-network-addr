# Typing
from ipaddress import ip_address
from typing import Dict


# Classes
class IpParser:
    def get_network_address(self, ip_to_parse: str) -> Dict[str, str]:
        '''
            A method to get the network address using the ip and
            his mask.
        '''
        ip_bin = self.__convert_ip_to_bin_ip(ip_to_parse[0])
        self.__write_content('Bin ip', self.__split_ip_with_dot(ip_bin, 8))

        mask_bar = self.__get_bin_mask(int(ip_to_parse[1]))
        self.__write_content('Bin mask', self.__split_ip_with_dot(mask_bar, 8))

        network_addr_bin = self.__get_bin_network_addr(ip_bin, mask_bar)
        network_addr_bin = self.__split_ip_with_dot(network_addr_bin, 8)
        self.__write_content('Bin network address', network_addr_bin)

        network_addr = self.__convert_byte_to_str(network_addr_bin)
        self.__write_content('Network address', network_addr)

    def __convert_ip_to_bin_ip(self, ip: str) -> str:
        '''
            Convert and typical ip to binary.
        '''
        ip_bin = ''
        for ip_div in ip.split('.'):
            bin_char = bin(int(ip_div)).replace('0b', '')
            if (len(bin_char) < 8):
                for x in range(8 - len(bin_char)):
                    bin_char = '0' + bin_char
            ip_bin += bin_char
        return ip_bin

    def __get_bin_mask(self, mask_bar: int) -> str:
        '''
            A method to get the mask form some ip.
        '''
        mask = ''.join(['1' for x in range(mask_bar)])

        if (len(mask) < 32):
            for x in range(32 - len(mask)):
                mask += '0'

        return mask

    def __split_ip_with_dot(self, ip_bin: str, count_on_div: int) -> str:
        '''
            A method to insert into the ip, the dot.
        '''
        ip_bin_div = ''
        for i in range(0, len(ip_bin), count_on_div):
            ip_bin_div += ip_bin[i:i+count_on_div] + '.'

        return ip_bin_div[:-1]

    def __get_bin_network_addr(self, ip: str, mask: str) -> str:
        '''
            A method to get the network address.
            @returns the network address as bin
        '''
        network_addr = ''
        for index, char_ip in enumerate(ip):
            if int(char_ip) == 1 and char_ip == mask[index]:
                network_addr += '1'
            else:
                network_addr += '0'
        return network_addr

    def __convert_byte_to_str(self, network_addr_bin: str) -> str:
        '''
            A method to convert the network address to string.
        '''
        # Convert the byte str to int
        network_addr = '' 
        for byte in network_addr_bin.split('.'):
            byte_dec = int(byte, 2)
            network_addr += f'{str(byte_dec)}.'
        network_addr = network_addr[:-1]
        return network_addr

    def __write_content(self, title: str, content: str):
        '''
            A method to write the content in a file.
        '''
        print(
        '{:<20}'.format(f'{title}: '), content)



# Code
ip_to_parse = input(
    'Enter the ip using the format: ip.ip.ip.ip/mask'
    '\n\nIp: ').split('/')

if (len(ip_to_parse) != 2):
    exit('Need to define an ip and his mask.')

ip_parser = IpParser()
ip_parser.get_network_address(ip_to_parse)
