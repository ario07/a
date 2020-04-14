ó
v~^c        
   @   s  d  Z  d d l Z d d l Z d Z d Z d Z d a e j Z d e	 f d     YZ
 d e
 f d	     YZ d
 e
 f d     YZ d e
 f d     YZ d e
 f d     YZ d e
 f d     YZ d- Z d. Z d/ Z d0 Z d d d e d d d*  Z d+ e j f d,     YZ d S(1   s  SocksiPy - Python SOCKS module.
Version 1.00

Copyright 2006 Dan-Haim. All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
3. Neither the name of Dan Haim nor the names of his contributors may be used
   to endorse or promote products derived from this software without specific
   prior written permission.
   
THIS SOFTWARE IS PROVIDED BY DAN HAIM "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL DAN HAIM OR HIS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA
OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMANGE.


This module provides a standard socket-like interface for Python
for tunneling connections through SOCKS proxies.

iÿÿÿÿNi   i   i   t
   ProxyErrorc           B   s   e  Z d    Z d   Z RS(   c         C   s   | |  _  d  S(   N(   t   value(   t   selfR   (    (    s!   /storage/emulated/0/ddos/socks.pyt   __init__,   s    c         C   s   t  |  j  S(   N(   t   reprR   (   R   (    (    s!   /storage/emulated/0/ddos/socks.pyt   __str__.   s    (   t   __name__t
   __module__R   R   (    (    (    s!   /storage/emulated/0/ddos/socks.pyR    +   s   	t   GeneralProxyErrorc           B   s   e  Z d    Z d   Z RS(   c         C   s   | |  _  d  S(   N(   R   (   R   R   (    (    s!   /storage/emulated/0/ddos/socks.pyR   2   s    c         C   s   t  |  j  S(   N(   R   R   (   R   (    (    s!   /storage/emulated/0/ddos/socks.pyR   4   s    (   R   R   R   R   (    (    (    s!   /storage/emulated/0/ddos/socks.pyR   1   s   	t   Socks5AuthErrorc           B   s   e  Z d    Z d   Z RS(   c         C   s   | |  _  d  S(   N(   R   (   R   R   (    (    s!   /storage/emulated/0/ddos/socks.pyR   8   s    c         C   s   t  |  j  S(   N(   R   R   (   R   (    (    s!   /storage/emulated/0/ddos/socks.pyR   :   s    (   R   R   R   R   (    (    (    s!   /storage/emulated/0/ddos/socks.pyR	   7   s   	t   Socks5Errorc           B   s   e  Z d    Z d   Z RS(   c         C   s   | |  _  d  S(   N(   R   (   R   R   (    (    s!   /storage/emulated/0/ddos/socks.pyR   >   s    c         C   s   t  |  j  S(   N(   R   R   (   R   (    (    s!   /storage/emulated/0/ddos/socks.pyR   @   s    (   R   R   R   R   (    (    (    s!   /storage/emulated/0/ddos/socks.pyR
   =   s   	t   Socks4Errorc           B   s   e  Z d    Z d   Z RS(   c         C   s   | |  _  d  S(   N(   R   (   R   R   (    (    s!   /storage/emulated/0/ddos/socks.pyR   D   s    c         C   s   t  |  j  S(   N(   R   R   (   R   (    (    s!   /storage/emulated/0/ddos/socks.pyR   F   s    (   R   R   R   R   (    (    (    s!   /storage/emulated/0/ddos/socks.pyR   C   s   	t	   HTTPErrorc           B   s   e  Z d    Z d   Z RS(   c         C   s   | |  _  d  S(   N(   R   (   R   R   (    (    s!   /storage/emulated/0/ddos/socks.pyR   J   s    c         C   s   t  |  j  S(   N(   R   R   (   R   (    (    s!   /storage/emulated/0/ddos/socks.pyR   L   s    (   R   R   R   R   (    (    (    s!   /storage/emulated/0/ddos/socks.pyR   I   s   	t   successs   invalid datas   not connecteds   not availables   bad proxy types	   bad inputt	   succeededs   general SOCKS server failures!   connection not allowed by rulesets   Network unreachables   Host unreachables   Connection refuseds   TTL expireds   Command not supporteds   Address type not supporteds   Unknown errors   authentication is requireds0   all offered authentication methods were rejecteds$   unknown username or invalid passwords   unknown errors   request granteds   request rejected or failedsL   request rejected because SOCKS server cannot connect to identd on the clientsP   request rejected because the client program and identd report different user-idsc         C   s   |  | | | | | f a  d S(   s«   setdefaultproxy(proxytype, addr[, port[, rdns[, username[, password]]]])
	Sets a default proxy which all further socksocket objects will use,
	unless explicitly changed.
	N(   t   _defaultproxy(   t	   proxytypet   addrt   portt   rdnst   usernamet   password(    (    s!   /storage/emulated/0/ddos/socks.pyt   setdefaultproxym   s    t
   socksocketc           B   s   e  Z d  Z e j e j d d d  Z d   Z d d d e	 d d d  Z
 d   Z d   Z d   Z d   Z d	   Z d
   Z d   Z RS(   s÷   socksocket([family[, type[, proto]]]) -> socket object
	
	Open a SOCKS enabled socket. The parameters are the same as
	those of the standard socket init. In order for SOCKS to work,
	you must specify family=AF_INET, type=SOCK_STREAM and proto=0.
	i    c         C   sP   t  j |  | | | |  t d  k r1 t |  _ n	 d |  _ d  |  _ d  |  _ d  S(   N(   NNNNNN(   t
   _orgsocketR   R   t   Nonet   _socksocket__proxyt   _socksocket__proxysocknamet   _socksocket__proxypeername(   R   t   familyt   typet   protot   _sock(    (    s!   /storage/emulated/0/ddos/socks.pyR   }   s    		c         C   s@   d } x3 t  |  | k  r; | |  j | t  |   } q	 W| S(   s   __recvall(bytes) -> data
		Receive EXACTLY the number of bytes requested from the socket.
		Blocks until the required number of bytes have been received.
		t    (   t   lent   recv(   R   t   bytest   data(    (    s!   /storage/emulated/0/ddos/socks.pyt	   __recvall   s    !c         C   s   | | | | | | f |  _  d S(   s  setproxy(proxytype, addr[, port[, rdns[, username[, password]]]])
		Sets the proxy to be used.
		proxytype -	The type of the proxy to be used. Three types
				are supported: PROXY_TYPE_SOCKS4 (including socks4a),
				PROXY_TYPE_SOCKS5 and PROXY_TYPE_HTTP
		addr -		The address of the server (IP or DNS).
		port -		The port of the server. Defaults to 1080 for SOCKS
				servers and 8080 for HTTP proxy servers.
		rdns -		Should DNS queries be preformed on the remote side
				(rather than the local side). The default is True.
				Note: This has no effect with SOCKS4 servers.
		username -	Username to authenticate with to the server.
				The default is no authentication.
		password -	Password to authenticate with to the server.
				Only relevant when username is also provided.
		N(   R   (   R   R   R   R   R   R   R   (    (    s!   /storage/emulated/0/ddos/socks.pyt   setproxy   s    c   
      C   s  |  j  d d k r6 |  j  d d k r6 |  j d  n |  j d  |  j d  } | d d k r |  j   t d t d f   n  | d d	 k r n| d d
 k rn|  j d t t |  j  d   |  j  d t t |  j	 d   |  j  d  |  j d  } | d d k r;|  j   t d t d f   n  | d d	 k r·|  j   t
 d t d f  q·nI |  j   | d d k r¡t
 d t d f   n t d t d f   d } y! t j |  } | d | } Wnt t j k
 rT|  j  d t k r+d } | d t t |   | } qUt j t j |   } | d | } n X| t j d |  } |  j |  |  j d  } | d d k rº|  j   t d t d f   në | d d	 k r*|  j   t | d  d k rt t | d  t t | d    q¥t d t d   n{ | d d k rL|  j d  } nY | d d k r| |  j d  } |  j | d  } n  |  j   t d t d f   t j d |  j d   d }	 | |	 f |  _ | d k rút j |  | f |  _ n | | f |  _ d S(   s_   __negotiatesocks5(self,destaddr,destport)
		Negotiates a connection through a SOCKS5 server.
		i   i   s    s    i   i    s   i   s    s   s   i   s   ÿs   s   >Hi   i	   N(   R   R   t   sendallt   _socksocket__recvallt   closeR   t   _generalerrorst   chrR"   t   proxyR	   t   _socks5autherrorst   sockett	   inet_atont   errort   Truet   gethostbynamet   structt   packt   ordR
   R#   t   unpackR   t	   inet_ntoaR   (
   R   t   destaddrt   destportt
   chosenautht   authstatt   reqt   ipaddrt   respt	   boundaddrt	   boundport(    (    s!   /storage/emulated/0/ddos/socks.pyt   __negotiatesocks5£   sn    &
Q


!

*
c         C   s   |  j  S(   s]   getsockname() -> address info
		Returns the bound IP address and port number at the proxy.
		(   R   (   R   (    (    s!   /storage/emulated/0/ddos/socks.pyt   getproxysocknameÿ   s    c         C   s   t  j |   S(   sT   getproxypeername() -> address info
		Returns the IP and port number of the proxy.
		(   R   t   getpeername(   R   (    (    s!   /storage/emulated/0/ddos/socks.pyt   getproxypeername  s    c         C   s   |  j  S(   s   getpeername() -> address info
		Returns the IP address and port number of the destination
		machine (note: getproxypeername returns the proxy)
		(   R   (   R   (    (    s!   /storage/emulated/0/ddos/socks.pyRD     s    c         C   s  t  } y t j |  } WnN t j k
 ri |  j d t k rN d } t } qj t j t j |   } n Xd t j d |  | } |  j d d k r« | |  j d } n  | d } | t k rÒ | | d } n  |  j
 |  |  j d  } | d d k r!|  j   t d	 t d	 f   n  | d	 d
 k r¥|  j   t | d	  d k r|  j   t t | d	  t t | d	  d f   q¥t d t d f   n  t j | d  t j d | d d ! d f |  _ | d k rÿt j |  | f |  _ n | | f |  _ d S(   s_   __negotiatesocks4(self,destaddr,destport)
		Negotiates a connection through a SOCKS4 server.
		i   s      s   s   >Hi   s    i   i    i   t   Zi[   i\   i]   iZ   i^   i   N(   i[   i\   i]   (   t   FalseR/   R0   R1   R   R2   R3   R4   R5   R   R(   R)   R*   R   R+   R6   R   t   _socks4errorsR8   R7   R   R   (   R   R9   R:   t   rmtrslvR>   R=   R?   (    (    s!   /storage/emulated/0/ddos/socks.pyt   __negotiatesocks4  s:    	



13c         C   sz  |  j  d t k r% t j |  } n | } |  j d | d t |  d d | d  |  j d  } x, | j d  d k r | |  j d  } ql W| j   d	 j	 d
 d  } | d	 d k rç |  j
   t d t d f   n  y t | d  } Wn1 t k
 r.|  j
   t d t d f   n X| d k r^|  j
   t | | d f   n  d |  _ | | f |  _ d S(   s\   __negotiatehttp(self,destaddr,destport)
		Negotiates a connection through an HTTP server.
		i   s   CONNECT t   :s    HTTP/1.1
s   Host: s   

i   iÿÿÿÿi    t    i   s   HTTP/1.0s   HTTP/1.1iÈ   s   0.0.0.0N(   s   HTTP/1.0s   HTTP/1.1(   s   0.0.0.0i    (   R   RG   R/   R3   R(   t   strR#   t   findt
   splitlinest   splitR*   R   R+   t   intt
   ValueErrorR   R   R   (   R   R9   R:   R   R?   t
   statuslinet
   statuscode(    (    s!   /storage/emulated/0/ddos/socks.pyt   __negotiatehttpB  s*    /


	c         C   s)  t  |  t t f k o# t k n sf t |  d k  sf t  | d  t k sf t  | d  t k r t d t d f   n  |  j	 d t
 k ró |  j	 d d k rµ |  j	 d } n d } t j |  |  j	 d | f  |  j | d | d  n2|  j	 d t k rg|  j	 d d k r)|  j	 d } n d } t j |  |  j	 d | f  |  j | d | d  n¾ |  j	 d t k rÛ|  j	 d d k r|  j	 d } n d } t j |  |  j	 d | f  |  j | d | d  nJ |  j	 d d k rt j |  | d | d f  n t d t d f   d S(	   sà   connect(self,despair)
		Connects to the specified destination through a proxy.
		destpar - A tuple of the IP/DNS address and the port number.
		(identical to socket's connect).
		To select the proxy server use setproxy().
		i   i    i   i   i8  i  i   N(   R   t   listt   tupleRG   R"   RM   RQ   R   R+   R   t   PROXY_TYPE_SOCKS5R   R   t   connectt   _socksocket__negotiatesocks5t   PROXY_TYPE_SOCKS4t   _socksocket__negotiatesocks4t   PROXY_TYPE_HTTPt   _socksocket__negotiatehttp(   R   t   destpairt   portnum(    (    s!   /storage/emulated/0/ddos/socks.pyRY   a  s.    f!N(   R   R   t   __doc__R/   t   AF_INETt   SOCK_STREAMR   R   R)   R2   R'   RZ   RC   RE   RD   R\   R^   RY   (    (    (    s!   /storage/emulated/0/ddos/socks.pyR   u   s   		
	\				0	(   R   s   invalid datas   not connecteds   not availables   bad proxy types	   bad input(
   R   s   general SOCKS server failures!   connection not allowed by rulesets   Network unreachables   Host unreachables   Connection refuseds   TTL expireds   Command not supporteds   Address type not supporteds   Unknown error(   R   s   authentication is requireds0   all offered authentication methods were rejecteds$   unknown username or invalid passwords   unknown error(   s   request granteds   request rejected or failedsL   request rejected because SOCKS server cannot connect to identd on the clientsP   request rejected because the client program and identd report different user-idss   unknown error(   Ra   R/   R4   R[   RX   R]   R   R   R   t	   ExceptionR    R   R	   R
   R   R   R+   t   _socks5errorsR.   RH   R2   R   R   (    (    (    s!   /storage/emulated/0/ddos/socks.pyt   <module>   sR   	                      