DEBUG: Using selector: KqueueSelector
INFO: Datagram endpoint local_addr=('0.0.0.0', 30303) remote_addr=None created: (<_SelectorDatagramTransport fd=8 read=idle write=<idle, bufsize=0>>, <__main__.DiscoveryProtocol object at 0x102be70b8>)
DEBUG: boostrapping with [<Node(0x78de@191.235.84.50)>, <Node(0x158f@13.75.154.138)>, <Node(0x1118@52.74.57.123)>]

###################################################
# Attempting to conact the three bootstrap nodes
###################################################
DEBUG: >>> pinging <Node(0x158f@13.75.154.138)>
DEBUG: >>> pinging <Node(0x78de@191.235.84.50)>
DEBUG: >>> pinging <Node(0x1118@52.74.57.123)>

DEBUG: poll 889.589 ms took 128.876 ms: 1 events
DEBUG: <<< pong from <Node(0x78de@191.235.84.50)>
DEBUG: got expected pong with pingid 0x8f45501c6914584dc436ed44a581a14f0b8d4e87036ada2eb1389e96e7e55a3178de8a0916848093c73790ead81d1928bec737d565119932b98c6b100d944b7a95e94f847f689fc723399d2e31129d182f7ef3863f2b4c820abbf3ab2722344d
DEBUG: poll 743.289 ms took 56.322 ms: 1 events
DEBUG: <<< pong from <Node(0x158f@13.75.154.138)>
DEBUG: got expected pong with pingid 0x700f704535a87521c7187b950e7f0c9152229cb86205892a115074b176bfca56158f8aab45f6d19c6cbf4a089c2670541a8da11978a2f90dbf6a502a4a3bab80d288afdbeb7ec0ef6d92de563767f3b1ea9e8e334ca711e9f8e2df5a0385e8e6
DEBUG: poll 679.370 ms took 45.909 ms: 1 events
DEBUG: <<< pong from <Node(0x1118@52.74.57.123)>
DEBUG: got expected pong with pingid 0x69e5c9c772ebdbc25856e12e7452dd6e1f6d09299f259711f54cfce86a734f871118980bf48b0a3640bdba04e0fe78b1add18e1cd99bf22d53daac1fd9972ad650df52176e7c7d89d1114cfef2bc23a2959aa54998a46afcf7d91809f0855082
DEBUG: timed out waiting for ping from <Node(0x78de@191.235.84.50)>
DEBUG: bonding completed successfully with <Node(0x78de@191.235.84.50)>
DEBUG: timed out waiting for ping from <Node(0x158f@13.75.154.138)>
DEBUG: bonding completed successfully with <Node(0x158f@13.75.154.138)>
DEBUG: timed out waiting for ping from <Node(0x1118@52.74.57.123)>
DEBUG: bonding completed successfully with <Node(0x1118@52.74.57.123)>
###################################################
# Finished connecting with all three bootstrap nodes
###################################################


###################################################
# Node Lookup -> asking bootstrap nodes who is close to me
###################################################
DEBUG: starting lookup; initial neighbours: [<Node(0x158f@13.75.154.138)>, <Node(0x1118@52.74.57.123)>, <Node(0x78de@191.235.84.50)>]
DEBUG: node lookup; querying [<Node(0x158f@13.75.154.138)>, <Node(0x1118@52.74.57.123)>, <Node(0x78de@191.235.84.50)>]
DEBUG: >>> find_node to <Node(0x1118@52.74.57.123)>
DEBUG: >>> find_node to <Node(0x158f@13.75.154.138)>
DEBUG: >>> find_node to <Node(0x78de@191.235.84.50)>
DEBUG: poll 889.104 ms took 133.738 ms: 1 events
DEBUG: <<< neighbours from <Node(0x78de@191.235.84.50)>: [<Node(0xca6a@136.243.66.23)>, <Node(0x909e@173.33.215.109)>, <Node(0xa6c1@87.211.59.234)>, <Node(0xfd20@86.62.74.149)>, <Node(0x0136@188.32.187.192)>, <Node(0x9293@45.79.64.234)>, <Node(0xd4c6@185.92.185.85)>, <Node(0x9053@68.77.36.20)>, <Node(0x65b9@113.22.194.146)>, <Node(0x4721@174.138.37.251)>, <Node(0x99f7@77.160.215.46)>, <Node(0x22f2@46.200.69.208)>]
DEBUG: poll 735.039 ms took 0.026 ms: 1 events
DEBUG: <<< neighbours from <Node(0x78de@191.235.84.50)>: [<Node(0xe838@136.24.174.5)>, <Node(0x41d5@79.165.17.83)>, <Node(0x7fd5@210.180.118.188)>, <Node(0x1c56@18.216.138.222)>]
DEBUG: got expected neighbours response from <Node(0x78de@191.235.84.50)>
###################################################
# Received 16 candidates from one of node 0x78
# Attempting to bond with all 16
###################################################
DEBUG: got 16 new candidates
DEBUG: >>> pinging <Node(0x9053@68.77.36.20)>
DEBUG: >>> pinging <Node(0x41d5@79.165.17.83)>
DEBUG: >>> pinging <Node(0xfd20@86.62.74.149)>
DEBUG: >>> pinging <Node(0x7fd5@210.180.118.188)>
DEBUG: >>> pinging <Node(0xd4c6@185.92.185.85)>
DEBUG: >>> pinging <Node(0xa6c1@87.211.59.234)>
DEBUG: >>> pinging <Node(0x1c56@18.216.138.222)>
DEBUG: >>> pinging <Node(0x65b9@113.22.194.146)>
DEBUG: >>> pinging <Node(0x0136@188.32.187.192)>
DEBUG: >>> pinging <Node(0x4721@174.138.37.251)>
DEBUG: >>> pinging <Node(0xca6a@136.243.66.23)>
DEBUG: >>> pinging <Node(0x99f7@77.160.215.46)>
DEBUG: >>> pinging <Node(0x909e@173.33.215.109)>
DEBUG: >>> pinging <Node(0x22f2@46.200.69.208)>
DEBUG: >>> pinging <Node(0xe838@136.24.174.5)>
DEBUG: >>> pinging <Node(0x9293@45.79.64.234)>
DEBUG: <<< neighbours from <Node(0x158f@13.75.154.138)>: [<Node(0xca6a@136.243.66.23)>, <Node(0x57bc@72.38.69.182)>, <Node(0xfe3b@89.173.37.242)>, <Node(0xd8c3@35.189.249.117)>, <Node(0x0dbf@210.55.87.47)>, <Node(0x4cff@104.198.198.45)>, <Node(0x79fc@172.104.80.56)>, <Node(0x43dd@146.148.112.168)>, <Node(0x4a48@139.59.111.210)>, <Node(0x9a99@85.246.7.145)>, <Node(0x7505@18.54.7.133)>, <Node(0x78da@185.18.60.101)>]
DEBUG: poll 622.016 ms took 0.016 ms: 1 events
DEBUG: <<< neighbours from <Node(0x158f@13.75.154.138)>: [<Node(0xa8ac@59.173.0.226)>, <Node(0xabaa@137.59.252.141)>, <Node(0xac6b@13.72.242.46)>, <Node(0x851b@146.185.148.110)>]
DEBUG: <<< pong from <Node(0x4721@174.138.37.251)>
DEBUG: <<< neighbours from <Node(0x1118@52.74.57.123)>: [<Node(0xed39@52.230.20.62)>, <Node(0x83c3@165.227.214.75)>, <Node(0x949a@68.84.96.127)>, <Node(0x6d01@84.163.230.214)>, <Node(0x9c65@188.166.223.208)>, <Node(0xc474@78.46.109.62)>, <Node(0xd4c6@185.92.185.85)>, <Node(0xb78c@159.203.66.105)>, <Node(0x81f9@84.104.175.24)>, <Node(0x1e1b@47.95.225.87)>, <Node(0x014b@137.59.67.2)>, <Node(0x21db@46.43.3.35)>]
DEBUG: got expected neighbours response from <Node(0x158f@13.75.154.138)>
DEBUG: got 15 new candidates
###################################################
# Received 15 candidates from one of node 0x158f
# Attempting to bond with all 15
###################################################
DEBUG: <<< neighbours from <Node(0x1118@52.74.57.123)>: [<Node(0xb0ec@86.153.179.181)>, <Node(0x4b57@13.64.146.159)>, <Node(0x48cf@174.65.167.20)>, <Node(0x563a@96.231.18.154)>]
DEBUG: >>> pinging <Node(0x7505@18.54.7.133)>
DEBUG: >>> pinging <Node(0x79fc@172.104.80.56)>
DEBUG: >>> pinging <Node(0xd8c3@35.189.249.117)>
DEBUG: >>> pinging <Node(0x4a48@139.59.111.210)>
DEBUG: >>> pinging <Node(0x9a99@85.246.7.145)>
DEBUG: >>> pinging <Node(0x78da@185.18.60.101)>
DEBUG: >>> pinging <Node(0xac6b@13.72.242.46)>
DEBUG: >>> pinging <Node(0x0dbf@210.55.87.47)>
DEBUG: >>> pinging <Node(0x851b@146.185.148.110)>
DEBUG: >>> pinging <Node(0x57bc@72.38.69.182)>
DEBUG: >>> pinging <Node(0x4cff@104.198.198.45)>
DEBUG: >>> pinging <Node(0xfe3b@89.173.37.242)>
DEBUG: >>> pinging <Node(0x43dd@146.148.112.168)>
DEBUG: >>> pinging <Node(0xabaa@137.59.252.141)>
DEBUG: >>> pinging <Node(0xa8ac@59.173.0.226)>
DEBUG: got expected pong with pingid 0x9438f7e53a031dad67b340864b70d278d70dd3625bca8790129ff38211fac8214721d03a51b262838493a58ff95db094a6825affc6eb681fd28657cc2d5140f6b10eddd844044ecacb56661c76e2d5434dd1fd220c7b7af63ee43dc986954a6b
DEBUG: <<< pong from <Node(0x41d5@79.165.17.83)>
DEBUG: <<< ping from <Node(0x41d5@79.165.17.83)>
DEBUG: >>> ponging <Node(0x41d5@79.165.17.83)>
DEBUG: got expected neighbours response from <Node(0x1118@52.74.57.123)>
###################################################
# Received 15 candidates from one of node 0x158f
# Attempting to bond with all 15
###################################################
DEBUG: got 15 new candidates
DEBUG: <<< pong from <Node(0x9293@45.79.64.234)>
DEBUG: >>> pinging <Node(0x48cf@174.65.167.20)>
DEBUG: >>> pinging <Node(0x563a@96.231.18.154)>
DEBUG: >>> pinging <Node(0xc474@78.46.109.62)>
DEBUG: >>> pinging <Node(0x9c65@188.166.223.208)>
DEBUG: >>> pinging <Node(0xb0ec@86.153.179.181)>
DEBUG: >>> pinging <Node(0x4b57@13.64.146.159)>
DEBUG: >>> pinging <Node(0x6d01@84.163.230.214)>
DEBUG: >>> pinging <Node(0xb78c@159.203.66.105)>
DEBUG: >>> pinging <Node(0x83c3@165.227.214.75)>
DEBUG: >>> pinging <Node(0x949a@68.84.96.127)>
DEBUG: >>> pinging <Node(0xed39@52.230.20.62)>
DEBUG: >>> pinging <Node(0x81f9@84.104.175.24)>
DEBUG: >>> pinging <Node(0x014b@137.59.67.2)>
DEBUG: >>> pinging <Node(0x1e1b@47.95.225.87)>
DEBUG: >>> pinging <Node(0x21db@46.43.3.35)>
DEBUG: got expected pong with pingid 0xed80d3979ae63cb84c8c612fe23f41096c63de7063619626b04e9931bee7b6d241d5b1ace646272c8f9af3d65c2e161580aa67867e1f6b6c975ef0346366f6278fec905ffa7e711465a627229f3b117aa7aa89300861fa1075cdc6bd31be1b84
DEBUG: <<< pong from <Node(0xca6a@136.243.66.23)>
DEBUG: <<< pong from <Node(0x0136@188.32.187.192)>
DEBUG: got expected pong with pingid 0x432b6ce28cb2ae0de35f2486d8c841006b368a4831d7a7d39046a78ca30ff6999293d4d996e92a8fd39552facaca602acad127b420893b3c7fc7c30ec955c3ee6eafe7d30aa527c348f0cd001a9abd4047729d8514d3d205a3affbb0b644c04f
DEBUG: <<< pong from <Node(0x7505@18.54.7.133)>
DEBUG: unexpected pong from <Node(0x7505@18.54.7.133)> with pingid 0x7e5dddda9e85e6a3bc2380fd4f3c726a2cbb4002be6caf00bd2e7b72a8e765db7505c74e9010d092a1c525cc0485949288ce0c5186a7f8e88d2dd826a39a6440c980846fc0804cabca436e9eb45860d7e6f7863ae309e3c1c01a5d3fa229a004, probably came too late
DEBUG: got expected pong with pingid 0xaf5c126349502e0b01edd5a8601e2b9a142bc1259b6f6ff09ff1e49f6426b047ca6adf20b52a1f284b78a8c811d1e76615b9a1ff9107802aa95778b7f001ef6aea753f1e71c59ea4f0fc14c73c78fde3073997b04e61111638c35a273577783c
DEBUG: <<< pong from <Node(0x7fd5@210.180.118.188)>
DEBUG: unexpected pong from <Node(0x7fd5@210.180.118.188)> with pingid 0x23f0402f763aec8430d61c4235337ff17edbd6ed19ff502c28b583e18141ff187fd5c6e52d3622b98ab622d9d20086a4e33db3e06b0810c1090161e059ce9093870401ca14943420ea68d6021629a7f4572b0defadaddadeb75ac4381396a3d1, probably came too late
DEBUG: got expected pong with pingid 0x5ab4837476f8fac55e762f9d868737423d4c1d874b666ec6743d9044590ec0ca013645b6895de871f9f9b49e7e727d65e84de34c40701203540c466ee0a0431eebbf12f9bef72541a19a3812f76e1579da81aa2b1b88f96a554098d1c12ac6b8
DEBUG: <<< pong from <Node(0x57bc@72.38.69.182)>
DEBUG: <<< pong from <Node(0xd8c3@35.189.249.117)>
DEBUG: <<< ping from <Node(0x9293@45.79.64.234)>
DEBUG: >>> ponging <Node(0x9293@45.79.64.234)>
DEBUG: got expected pong with pingid 0xa76c6f9615fd772cd6d61aa4b6abdec9fa2fc6bfd01dd977ece058f1f578aeb257bcfb52d41e3483af0d5b121e21c7e8b2546af9a4842259cc034f606613458757aa96d4576f60d194a45d553e18533fd8e63cae3aa816db5ed1af49423810d3
DEBUG: <<< pong from <Node(0x9a99@85.246.7.145)>
DEBUG: unexpected pong from <Node(0x9a99@85.246.7.145)> with pingid 0x58b04f96e4a3356bb8774cf87c6ce11a534d1a9a618850925d9fdc6692d14d239a9959ea634f9bf04e111a7ddbcdef60639141ff5d96c3b989348075b41ac2cd8363af61dab40149f39fb63ae0a24ac15c82ee274bbb3748db86ab08e8850b4e, probably came too late
DEBUG: got expected pong with pingid 0xe0fdc8d6dc807595742c0f5c7d18569aeb731694d5ab4a11d67d47e68e98ec5fd8c3635e6afd7395dee22d27249ad989d1910f8c13c4062be22e9bd6e800575b495aecaf62dc9a9b20aa782023831f12d4a9acc99a418cff2b098c4e97ef49d2
DEBUG: <<< pong from <Node(0x43dd@146.148.112.168)>
DEBUG: got expected ping from <Node(0x9293@45.79.64.234)>
DEBUG: bonding completed successfully with <Node(0x9293@45.79.64.234)>
DEBUG: <<< pong from <Node(0x79fc@172.104.80.56)>
DEBUG: unexpected pong from <Node(0x79fc@172.104.80.56)> with pingid 0xf3d55ee33f7368154a4e9fe3af74fae176cdef7949b503778cd3ba153aa977a779fc0d0c0dd800d1b53c4d052ee0aa482ca55e6e8c80bc98b06e8e90fa9a49d6477b1238bfedea8c6a2a0bf4e86c8574aa24c99252ebd9dc542f74204d732045, probably came too late
DEBUG: <<< pong from <Node(0xb78c@159.203.66.105)>
DEBUG: got expected pong with pingid 0x9a86c62a3cee1c7a65c17dd3818ba0fb92006ddeb4e78a41f9b5095a8adaf1fe43ddeaa097fc63ded6d9addd5430faf4f5dac05143ed4ff67028923efa2b68e41d21c1136972d154680005f0844e44677e9cd484efbdc3f546bbddb6e5717477
DEBUG: <<< pong from <Node(0x83c3@165.227.214.75)>
DEBUG: <<< pong from <Node(0x4b57@13.64.146.159)>
DEBUG: got expected pong with pingid 0xcf5886d040602a7f8a81a2380f935bf40ac404900ef174e8cfd297a3e3b74310b78c81e433052bbdaaa7865a1d087b1388686df47853915588ca584927f2a357b01bd28c301c508c808ea3c3482914df33857dac6d4035093349c6e27f40268a
DEBUG: <<< ping from <Node(0x4b57@13.64.146.159)>
DEBUG: >>> ponging <Node(0x4b57@13.64.146.159)>
DEBUG: got expected pong with pingid 0x930bf80034865899f4e3d0528f3aa2991deaa9c314ff4b944526693f387b846083c31989e15d7b5c823c52bc9b68f685b699c9d0f43751d16ff7fa04a31021bb0b9464f842d925fb0c430776598c86dcdd587202a572195c3eef36e576bc95d0
DEBUG: <<< pong from <Node(0xac6b@13.72.242.46)>
DEBUG: got expected pong with pingid 0x0a35f9aaf13669f997be047204a169802ac87bae96c3f6774f62754ccae5f5e74b57668175dcbfa0abf9aa2028ac12ae12698e347b89051dfbaadb672a8406b00377218ae699de781630446f6d627e89a1d963ff18558ac8115ef0928e8b0d99
DEBUG: <<< ping from <Node(0xac6b@13.72.242.46)>
DEBUG: >>> ponging <Node(0xac6b@13.72.242.46)>
DEBUG: <<< pong from <Node(0x0dbf@210.55.87.47)>
DEBUG: got expected pong with pingid 0x71d51fb957e7330dce49280bb1fc3f01f9f702e95c766f7725502ff0dd952e90ac6b1096ca56b9f6d004b779ae3728bf83f8e22453404cc3cef16a3d9b96608bc67c4b30db88e0a5a6c6390213f7acbe1153ff6d23ce57380104288ae19373ef
DEBUG: <<< ping from <Node(0x0dbf@210.55.87.47)>
DEBUG: >>> ponging <Node(0x0dbf@210.55.87.47)>
DEBUG: <<< pong from <Node(0x4a48@139.59.111.210)>
DEBUG: got expected pong with pingid 0xf39c138a523dd06ff04452733d77fe9ffcf79a636cf95ca1eacaaa8447de30fd0dbf2a4ef0de6320c6f95807be84af30599b1a3478fe54b5d70e50bdb94eeec3fe30513e9b455a5953df624404b8be8ebf354f55263935604684b9988cfadb1a
DEBUG: <<< pong from <Node(0x21db@46.43.3.35)>
DEBUG: <<< ping from <Node(0x21db@46.43.3.35)>
DEBUG: >>> ponging <Node(0x21db@46.43.3.35)>
DEBUG: got expected pong with pingid 0x1db93c8d74b497ac3af82901ab56beb5f7dcd9fcc11d21a4af7f288d79ca69244a48a753dddce5022888eec9291d21e44e79c0707a18c3dca79cb7fede0d081797f07dfc8c9d11554eda77eb1bc26ff7bd35a33ea2c24e3174ca02e0bf9f840a
DEBUG: <<< pong from <Node(0x48cf@174.65.167.20)>
DEBUG: got expected pong with pingid 0xb016e584ee97060c0cd945a53a44c44855271273256d9b24bb8c80eab4ae91ad21dbc258fc3dfdc861fa9a943c18781a67ad21a6cb0c654a2d4faf4c64db4c6cbd1bf0bf9095f9b16bec331628a54c55e7bb58ba02686af3fc47d6c965387b47
DEBUG: <<< ping from <Node(0x48cf@174.65.167.20)>
DEBUG: >>> ponging <Node(0x48cf@174.65.167.20)>
DEBUG: <<< pong from <Node(0x9c65@188.166.223.208)>
DEBUG: got expected pong with pingid 0xfd226c8fbb9d631303ba01f4f42ed9b819decfb7be224478163dc7ad58a1868748cf3fc1861e95086f1d1377a318bce0f6920e9a91f6c03d3ce01961e8434ba9fbde614e79db209d9ef37dfbf6ebe00cd9b064a069fbd1af8ee4ea81d1be714d
DEBUG: <<< ping from <Node(0x9c65@188.166.223.208)>
DEBUG: >>> ponging <Node(0x9c65@188.166.223.208)>
DEBUG: <<< pong from <Node(0x1e1b@47.95.225.87)>
DEBUG: got expected pong with pingid 0x53d6dc936558c2f4350e4a8d238844cd07c3eab6392c557c6c962011df7107089c65d4e025d4288b8c26e82679678778e4efafc3faf134d741fd9a21ad593a249dbe629e4ecb7a8767b64c063c0afbab8e349cb82a50653d9dd6acdd75c3c08b
DEBUG: <<< ping from <Node(0x1e1b@47.95.225.87)>
DEBUG: >>> ponging <Node(0x1e1b@47.95.225.87)>
DEBUG: <<< ping from <Node(0xd8c3@35.189.249.117)>
DEBUG: >>> ponging <Node(0xd8c3@35.189.249.117)>
DEBUG: got expected pong with pingid 0xca3c49c83962d3e9faeb7cf7142f792ea334db0596037bc6a14dfcc1ebe686c21e1b85f21114c6640cd3b9ec876669b15c09b940f7c7f5410772812cade673ff0396b039f2991db22e7d1ce85863fbdc8d0809a332346e318fad916722c44957
DEBUG: got expected ping from <Node(0xd8c3@35.189.249.117)>
DEBUG: bonding completed successfully with <Node(0xd8c3@35.189.249.117)>
DEBUG: timed out waiting for pong with pingid 0x1ff069e419c09d2eb41f3704d43a55cd7e17813a075e7471d5294e67117b4fb89053fb06ffd3eb831c3874f10d40d520b3a943aa974f65596d4dd8f79a6bd5f05b21addef70e6d61afe04406a80ca5116d1e6e2598888612b6d183cc5a7bd608
DEBUG: bonding failed, didn't receive pong from <Node(0x9053@68.77.36.20)>
DEBUG: timed out waiting for pong with pingid 0x17989369380acba69c3cb230ee45a418340b60abf5903f296ad410f65d1f1dcafd200f16e98083cbd651075af0da5fffd87a18b6fa99b8a9aad2e71fdc5f5b2e4b6fab057c3457f2d4955062bead7cff14d51cee66dfcd776a8e4d392963ad76
DEBUG: bonding failed, didn't receive pong from <Node(0xfd20@86.62.74.149)>
DEBUG: timed out waiting for pong with pingid 0xbdbaa1005e59de01a0e6407a379a761fd10ce17eba7adff0a8dc2c5bf553593d7fd5c6e52d3622b98ab622d9d20086a4e33db3e06b0810c1090161e059ce9093870401ca14943420ea68d6021629a7f4572b0defadaddadeb75ac4381396a3d1
DEBUG: bonding failed, didn't receive pong from <Node(0x7fd5@210.180.118.188)>
DEBUG: timed out waiting for pong with pingid 0x228a200d0c1b6f3782bff73d8c4bd1b052cb343c48287ff03b59cdff5fafce0cd4c6c13d4b8f8b06039be6dbbe4c88ec547b6463f5684baf20b94ee5f8e8ac5b36291f1627a0a306e7e96a8c5c25349e43062ffbf28316bc8be3f55141745a40
DEBUG: bonding failed, didn't receive pong from <Node(0xd4c6@185.92.185.85)>
DEBUG: timed out waiting for pong with pingid 0x4f1ee3ced0244ae0a5b6ed11b13e10c3bf7ce7dde96e5d4f58319eb489e5f8f9a6c1ae5b753c78da2916fdee14952018cd2d33c02cf394bc4f7a93717870cfb4f1f19f4baae3b73f692a52b5797f398e91e73e206bbc959c688e7665d957834e
DEBUG: bonding failed, didn't receive pong from <Node(0xa6c1@87.211.59.234)>
DEBUG: timed out waiting for pong with pingid 0x09933acfc652dc7deae3d13caa174a46364f8a1ed7916dd9c6d3815a8d2e51701c561e872b7031940c0695ef422d5602dceed28b1adff0c4c3728c232b676a83ea9cb0a30eaf83f3e3532e3da9f4d58349d8d9fdbcd8b4aa970d7ab30a5fe546
DEBUG: bonding failed, didn't receive pong from <Node(0x1c56@18.216.138.222)>
DEBUG: timed out waiting for pong with pingid 0x370e16886a234de86e1b5971b3100a0956f1d97da913c87f159dfed045bfa75865b94800ab0e55ccbfdb42c77ab64fea80a655628b67be092ce9caabec47246a59cea9e37e2c2b7c2443105236a2588eecc77ed0fddaa11f2ca923f566d4da56
DEBUG: bonding failed, didn't receive pong from <Node(0x65b9@113.22.194.146)>
DEBUG: timed out waiting for pong with pingid 0xaef5c3f1bf11fda5c9f5013e174ebc84b9282d9f98c6c6ab3d07861fb7f3a80b99f73bd2648434f135be4f99745b9712560b8197c0b31ba2038070fffd1fbe936a0f44eeda137d6ffde8af286e1da58fc873f239d6e3e23cf3b7dd35097cbf01
DEBUG: bonding failed, didn't receive pong from <Node(0x99f7@77.160.215.46)>
DEBUG: timed out waiting for pong with pingid 0xbe3bce9b772f2c6b826e1a97ead418b330b95f8d2f3ce00020b2fa72989d6d77909e80fb76b4678b308007d7f3f953ce3fc1c07202160ab9756514b26f245efda3f1226f009717e4a699be140e7b94b952b3d9af31b4bb6bd2dc23c5ee624c9b
DEBUG: bonding failed, didn't receive pong from <Node(0x909e@173.33.215.109)>
DEBUG: timed out waiting for pong with pingid 0x7f8ad0a2c582f5e1d387660dbe11def664d9b661934d34f4e2927373a4c085c922f2afffb21dcb716a4e7b4767f7b833b5fc632fb38ab53ee5c38034f3b132d6778f6e8abf9f0c386b2174e9c33c899563da6dc50ef6cc6ac8979a39677bf9a3
DEBUG: bonding failed, didn't receive pong from <Node(0x22f2@46.200.69.208)>
DEBUG: timed out waiting for pong with pingid 0x2f5d04684b7f1cff127a7222ae04fd8476ce2413f020888116ad05ee12c98576e83877e057b12780f7951a049ead9d4cc4912442ce8f10324add7ed3e3f35a721788704f151c8b80b366256f2500a193bcdf5a80d7c1c7fe31b079a7bee7b830
DEBUG: bonding failed, didn't receive pong from <Node(0xe838@136.24.174.5)>
DEBUG: timed out waiting for pong with pingid 0x6982a08ee67b56dc87a556193f9c0498dd41f26b6d3f39634ce315d219eda2d27505c74e9010d092a1c525cc0485949288ce0c5186a7f8e88d2dd826a39a6440c980846fc0804cabca436e9eb45860d7e6f7863ae309e3c1c01a5d3fa229a004
DEBUG: bonding failed, didn't receive pong from <Node(0x7505@18.54.7.133)>
DEBUG: timed out waiting for pong with pingid 0x30168024ca9904fd4ae326a60522cc0df1f01033e1ce3b6056210d1f2ed3b75679fc0d0c0dd800d1b53c4d052ee0aa482ca55e6e8c80bc98b06e8e90fa9a49d6477b1238bfedea8c6a2a0bf4e86c8574aa24c99252ebd9dc542f74204d732045
DEBUG: bonding failed, didn't receive pong from <Node(0x79fc@172.104.80.56)>
DEBUG: timed out waiting for pong with pingid 0x8ae6851c3d6487b92cb340b34d62770ac335ad9a05a93f9661805d0f0b02e1fa9a9959ea634f9bf04e111a7ddbcdef60639141ff5d96c3b989348075b41ac2cd8363af61dab40149f39fb63ae0a24ac15c82ee274bbb3748db86ab08e8850b4e
DEBUG: bonding failed, didn't receive pong from <Node(0x9a99@85.246.7.145)>
DEBUG: timed out waiting for pong with pingid 0x03fb84a2f18ee179a772fc78d5fcdadeac3dcd95ccef157cbcfbf8d90ce4319178dacab6d2ac989c35ba9bde337b66ba17ad97753813ef92dc3834a1b0961d1e1bc7da1114f4ae9962f573205c8bcd90d8a25ce74db9f904c95c8f4077da1be7
DEBUG: bonding failed, didn't receive pong from <Node(0x78da@185.18.60.101)>
DEBUG: timed out waiting for pong with pingid 0x6fd4fcedf66c17b1fa2afdc058eeefbb112c90d812bf9fd38c76001e5eb455db851b7358ae8a0b3b0204adcf37648884eccd94cc63b16f29fb4c5759576c178adeceaacba80fe2f779719f2b47a8b4b8e41782df2e5a65aedb068536e6a50027
DEBUG: bonding failed, didn't receive pong from <Node(0x851b@146.185.148.110)>
DEBUG: timed out waiting for pong with pingid 0x2400b3cfbfca004daac76acebd2b3dd97b85672bec9373b2576f6f21b98c1dd14cff6559f9918957a57c087efaf5a6c6a9b67cc65522e6b449f353a8379681d92804107ba8e7fad92aec1c56b0900b8e3ad7d2699fb25efcb58938c428dcc7bb
DEBUG: bonding failed, didn't receive pong from <Node(0x4cff@104.198.198.45)>
DEBUG: timed out waiting for pong with pingid 0x790607ce78ffef1a85c3d2384283a79b70083990d2f0e757da09906a81e95079fe3b03079308ee58c2747680124689f553e7ba4de440bf51c583b92bdb424434220655af65b2b47351366eae60782aebdb6303a076077124a370308747fe72a9
DEBUG: bonding failed, didn't receive pong from <Node(0xfe3b@89.173.37.242)>
DEBUG: timed out waiting for pong with pingid 0xacb37973d3ed4439a144e640cb572cfeabf9960215eb7237c4abef756bd6a4beabaa386124c6ac41f78b818e992cf9f08389ba3c7914fa4165a24c1865ba95814d741aede9031967008a044e40c2b765c8f50ef5663c198496362f0150950f85
DEBUG: bonding failed, didn't receive pong from <Node(0xabaa@137.59.252.141)>
DEBUG: timed out waiting for pong with pingid 0x51b0ed6ec8ad1d66e2462185c58bd9fc0ea776a198549ae218b71bec855ad85aa8ac604ff0c84054da27af66398e8a8a4184388a184375fc53e9f37493adf586b776fd9a00889d41e16a8bb890f37f8e7dac2738ec6137bd3d475565b3b08bd8
DEBUG: bonding failed, didn't receive pong from <Node(0xa8ac@59.173.0.226)>
DEBUG: timed out waiting for ping from <Node(0x4721@174.138.37.251)>
DEBUG: bonding completed successfully with <Node(0x4721@174.138.37.251)>
DEBUG: timed out waiting for pong with pingid 0x8ca343e45ff7021b2a744e9df06afa9f82b4fe65ce8d33da686d3439b573adfa563a3876fd3d184c76c889d8d1b8526c3936110d263af130305a7c1cb41e30fcb0e79740fe7f93dce72601ef8a8a2489e4a92f29084b8c1337623b41010bb371
DEBUG: bonding failed, didn't receive pong from <Node(0x563a@96.231.18.154)>
DEBUG: timed out waiting for pong with pingid 0x501b2b5c57dcc087b587d19a577ccbb767a13d62f581993cfe02e44e702a2b79c4749b29658e99f919eaff7186193c2e1a2dd772f059551fdfd8cf21ba55d8227981fae4660b1654ff6e705f0e4f7564a1717282b5edf21977c21ee8b5d61afd
DEBUG: bonding failed, didn't receive pong from <Node(0xc474@78.46.109.62)>
DEBUG: timed out waiting for pong with pingid 0x0d8bd50b0adb69da76f2c1d0d05ad5ac587bc08edd878fef19c06f9ad90fbb6bb0ec4f98086f9cbcade7abeccb47b3f7eab8d070f30a306f4ff2f06acb0949ce21656e1a6e733bf823df29f0d2e8002d02ee2bf5f8fbd5e9a57e9c119dc0ffc2
DEBUG: bonding failed, didn't receive pong from <Node(0xb0ec@86.153.179.181)>
DEBUG: timed out waiting for pong with pingid 0x909b8e706146f3f3ed126491301d5a91d7ba25331c0df4a6bd35b71d60eef66b6d01b9705e6d7b31fce2e0f95227672043d46db43555dd9b1618f5c7b33c38435626faf2445d43113da20e5ed4e15de6fe641074a2067701ea5afc961a303cff
DEBUG: bonding failed, didn't receive pong from <Node(0x6d01@84.163.230.214)>
DEBUG: timed out waiting for pong with pingid 0xa6581ea8de2e6f8ad2ae9ffd582b37f9c718a269b99efae31eefe508ee2753e2949ac9ed8d22e9ed216a992fd0eaaa4e9bd41c70a1204d3f1890e5f6f7edd9485dbd42072d5e3d3f02677f3e3993df0d672a639694fafee003e3256f48f6d070
DEBUG: bonding failed, didn't receive pong from <Node(0x949a@68.84.96.127)>
DEBUG: timed out waiting for pong with pingid 0x0fdfe694c6fcd32d5c6b5f40dd867c8a30bda57e121af7aaa7125e66a4263d40ed3913dc344de4c7046f9a87ffbac0bd2c26e4f9bec25d89e33315d2139f8bb6eb4d8264ee74f1b1b211b39a63a2a442567a3584e80e2f0016391e44bf842300
DEBUG: bonding failed, didn't receive pong from <Node(0xed39@52.230.20.62)>
DEBUG: timed out waiting for pong with pingid 0x4e5687259e3f65b35563710eb32d9db528cf79240b24e88e7bff6eea179f852581f9e0a80d7ab2023b862b4e82066abfe5ceb432b90c4a7cfd5d07f7fe2a18844fa1ecf686978f7373a95cf972a1a25e3ff10549f9ac3d810765c5b1c085cbd9
DEBUG: bonding failed, didn't receive pong from <Node(0x81f9@84.104.175.24)>
DEBUG: <<< ping from <Node(0x43dd@146.148.112.168)>
DEBUG: >>> ponging <Node(0x43dd@146.148.112.168)>
DEBUG: timed out waiting for pong with pingid 0x800ed382ade3406387e12a22b66925e8d924c286ad662db0ca4b1280e227282c014b35a3d197dad4b8f4958c8f119cd9c0682190f294fe8786811d8c811f80ef1a84c53cba83599cb2dd8e7840a6538a132fe431260828ee56880861015d0b7e
DEBUG: bonding failed, didn't receive pong from <Node(0x014b@137.59.67.2)>
DEBUG: timed out waiting for ping from <Node(0x41d5@79.165.17.83)>
DEBUG: bonding completed successfully with <Node(0x41d5@79.165.17.83)>
DEBUG: got expected ping from <Node(0x43dd@146.148.112.168)>
DEBUG: bonding completed successfully with <Node(0x43dd@146.148.112.168)>
DEBUG: timed out waiting for ping from <Node(0xca6a@136.243.66.23)>
DEBUG: bonding completed successfully with <Node(0xca6a@136.243.66.23)>
DEBUG: timed out waiting for ping from <Node(0x0136@188.32.187.192)>
DEBUG: bonding completed successfully with <Node(0x0136@188.32.187.192)>
DEBUG: bonded with 5 candidates
DEBUG: timed out waiting for ping from <Node(0x57bc@72.38.69.182)>
DEBUG: bonding completed successfully with <Node(0x57bc@72.38.69.182)>
DEBUG: timed out waiting for ping from <Node(0xb78c@159.203.66.105)>
DEBUG: bonding completed successfully with <Node(0xb78c@159.203.66.105)>
DEBUG: poll 13.979 ms took 6.323 ms: 1 events
DEBUG: <<< ping from <Node(0x4a48@139.59.111.210)>
DEBUG: >>> ponging <Node(0x4a48@139.59.111.210)>
DEBUG: timed out waiting for ping from <Node(0x83c3@165.227.214.75)>
DEBUG: bonding completed successfully with <Node(0x83c3@165.227.214.75)>
DEBUG: timed out waiting for ping from <Node(0x4b57@13.64.146.159)>
DEBUG: bonding completed successfully with <Node(0x4b57@13.64.146.159)>
DEBUG: got expected ping from <Node(0x4a48@139.59.111.210)>
DEBUG: bonding completed successfully with <Node(0x4a48@139.59.111.210)>
DEBUG: timed out waiting for ping from <Node(0xac6b@13.72.242.46)>
DEBUG: bonding completed successfully with <Node(0xac6b@13.72.242.46)>
DEBUG: timed out waiting for ping from <Node(0x0dbf@210.55.87.47)>
DEBUG: bonding completed successfully with <Node(0x0dbf@210.55.87.47)>
DEBUG: bonded with 6 candidates
DEBUG: timed out waiting for ping from <Node(0x21db@46.43.3.35)>
DEBUG: bonding completed successfully with <Node(0x21db@46.43.3.35)>
DEBUG: timed out waiting for ping from <Node(0x48cf@174.65.167.20)>
DEBUG: bonding completed successfully with <Node(0x48cf@174.65.167.20)>
DEBUG: timed out waiting for ping from <Node(0x9c65@188.166.223.208)>
DEBUG: bonding completed successfully with <Node(0x9c65@188.166.223.208)>
DEBUG: timed out waiting for ping from <Node(0x1e1b@47.95.225.87)>
DEBUG: bonding completed successfully with <Node(0x1e1b@47.95.225.87)>
DEBUG: bonded with 7 candidates

##################################################
# Bonded with sucessfully with some of the candidates sent back from bootstrap 
# nodes
# Begin Querying the nodes we sucessfully bonded with for more neighbors
##################################################

DEBUG: node lookup; querying [<Node(0x4a48@139.59.111.210)>, <Node(0x43dd@146.148.112.168)>, <Node(0x21db@46.43.3.35)>]
DEBUG: >>> find_node to <Node(0x43dd@146.148.112.168)>
DEBUG: >>> find_node to <Node(0x4a48@139.59.111.210)>
DEBUG: >>> find_node to <Node(0x21db@46.43.3.35)>
DEBUG: poll 889.774 ms took 62.306 ms: 1 events
DEBUG: <<< ping from <Node(0xca6a@136.243.66.23)>
DEBUG: >>> ponging <Node(0xca6a@136.243.66.23)>
DEBUG: poll 804.704 ms took 1.937 ms: 1 events
DEBUG: <<< neighbours from <Node(0x21db@46.43.3.35)>: [<Node(0x8e74@188.138.1.237)>, <Node(0x9039@108.39.204.189)>, <Node(0x647a@84.29.40.212)>, <Node(0x5c30@176.9.154.84)>, <Node(0x799f@209.239.115.237)>, <Node(0x690d@213.32.53.181)>, <Node(0x0116@159.203.112.81)>, <Node(0x3afd@109.173.122.169)>, <Node(0x7e0d@136.243.88.194)>, <Node(0xdcb5@86.147.176.149)>, <Node(0x75f7@68.146.250.100)>, <Node(0xaa57@94.130.129.84)>]
DEBUG: poll 784.832 ms took 0.015 ms: 1 events
DEBUG: <<< neighbours from <Node(0x21db@46.43.3.35)>: [<Node(0x3cec@5.9.9.40)>, <Node(0xf23b@169.50.227.54)>, <Node(0x1664@94.176.235.121)>, <Node(0x4d6b@176.28.19.157)>]
DEBUG: got expected neighbours response from <Node(0x21db@46.43.3.35)>
DEBUG: got 16 new candidates
DEBUG: >>> pinging <Node(0x8e74@188.138.1.237)>
DEBUG: >>> pinging <Node(0xdcb5@86.147.176.149)>
DEBUG: >>> pinging <Node(0x75f7@68.146.250.100)>
DEBUG: >>> pinging <Node(0x9039@108.39.204.189)>
DEBUG: >>> pinging <Node(0xaa57@94.130.129.84)>
DEBUG: >>> pinging <Node(0x647a@84.29.40.212)>
DEBUG: >>> pinging <Node(0x3cec@5.9.9.40)>
DEBUG: >>> pinging <Node(0x690d@213.32.53.181)>
DEBUG: >>> pinging <Node(0x3afd@109.173.122.169)>
DEBUG: >>> pinging <Node(0xf23b@169.50.227.54)>
DEBUG: >>> pinging <Node(0x1664@94.176.235.121)>
DEBUG: >>> pinging <Node(0x0116@159.203.112.81)>
DEBUG: >>> pinging <Node(0x4d6b@176.28.19.157)>
DEBUG: >>> pinging <Node(0x5c30@176.9.154.84)>
DEBUG: >>> pinging <Node(0x7e0d@136.243.88.194)>
DEBUG: >>> pinging <Node(0x799f@209.239.115.237)>
DEBUG: <<< pong from <Node(0x9039@108.39.204.189)>
DEBUG: <<< ping from <Node(0x9039@108.39.204.189)>
DEBUG: >>> ponging <Node(0x9039@108.39.204.189)>
DEBUG: <<< pong from <Node(0x0116@159.203.112.81)>
DEBUG: got expected pong with pingid 0x29bd623efed473a816ceb4dc1ea6b073440300ebeb0c31744e4c58036236fbc8903951bfaddc3ef09e03895e918651dddb803cdadc281e4486faab22ace37ff9120147c89af0afdc5c68f8586337f1dcb98841b58496280edc039c5ea0fe13ef
DEBUG: <<< ping from <Node(0x0116@159.203.112.81)>
DEBUG: >>> ponging <Node(0x0116@159.203.112.81)>
DEBUG: <<< pong from <Node(0x8e74@188.138.1.237)>
DEBUG: got expected pong with pingid 0x1d0490f0099dcd963cba01e09249d401d1bde7b27a7dc2c5498ea7669355257901164db9f03929e3e3d771e1240fcae20200cf4f27bfdb26e76169ff07f2c1a37b9e416b5c2ca6ce8f2bfcc31b7419d9618d66f2b36f55a2cb9e23b48c56fb3e
DEBUG: <<< pong from <Node(0x799f@209.239.115.237)>
DEBUG: <<< ping from <Node(0x799f@209.239.115.237)>
DEBUG: >>> ponging <Node(0x799f@209.239.115.237)>
DEBUG: got expected pong with pingid 0x85d9d7a61738258783d285040643a71318411222554742244948a8b84ec54d1e8e74cc085c670d205da7c5fe88e5bbc7ec600a025398df88a1482affc4973d74c477b52feba8c3c88e3ab9e0e48f90f5749491c10ab697caa112cfda7cf5dfcc
DEBUG: <<< pong from <Node(0xaa57@94.130.129.84)>
DEBUG: got expected pong with pingid 0x25a607a6f200de2d70290c2a97750770fad47bb5b27e0c986712fc491904a806799f2e8d83d1a2fbd2ead8e7fd4ad88152acdfba850ad6cd69f8b398b6508bda8f4f1459816307db21ed1644b6cd06bbe0d5883b6524599a09bb355a5bc4fd64
DEBUG: <<< ping from <Node(0xaa57@94.130.129.84)>
DEBUG: >>> ponging <Node(0xaa57@94.130.129.84)>
DEBUG: <<< pong from <Node(0x690d@213.32.53.181)>
DEBUG: got expected pong with pingid 0x9be07e3300a370f92725f5a3fabd17695081dd6449689754ad021f5a05e51fa0aa57f5e5787931603120e90a0a0d8b932dbb9af05053f2c1ad0e5421432768c4e5f0624481b298902f38eb42a9c7c531929235734dff3d7dc1518faf7a9185a9
DEBUG: <<< ping from <Node(0x690d@213.32.53.181)>
DEBUG: >>> ponging <Node(0x690d@213.32.53.181)>
DEBUG: <<< pong from <Node(0xf23b@169.50.227.54)>
DEBUG: got expected pong with pingid 0xbd7d9a589dc5c8e0437205f56aab8290cf1c67f0c7ebb5feeb72a4a91a0ed3cf690db490f15a366b15126f67221bbcb0d4a6e6089e96db13787e805d3d273f3ffeccabc8bd149e6bbf6a4ab4744ed51ab7723c129007348dd7e0ff9e91df064e
DEBUG: <<< pong from <Node(0x3cec@5.9.9.40)>
DEBUG: <<< pong from <Node(0x647a@84.29.40.212)>
DEBUG: got expected pong with pingid 0xe23543eb9935d689ca566bf14ee5180ed4900529cd6775d15927ab49023fb937f23bd82aab31271ed9fe58df91e5adf9ac5e24b85c9bcd8c2677769e124e7aad263debb8e29c6da37ce1a0d3556a261d884e9d4adfcddcbb6b0d258270bcc07d
DEBUG: <<< ping from <Node(0x647a@84.29.40.212)>
DEBUG: >>> ponging <Node(0x647a@84.29.40.212)>
DEBUG: got expected pong with pingid 0xd55f495e8445257b8225dea934a620ac770c83d9e3cba9e21d655d0eb462cc903cec2ea15f269165dfa0f4e9269e86937c9aa085e0329652e3588ad7dd238d07c5aa5d485c4747e4b65a24b9c62664b5b28dc6b54983d938aac4a952399f5250
DEBUG: <<< pong from <Node(0x4d6b@176.28.19.157)>
DEBUG: got expected pong with pingid 0x7a16e90c576ad5e5e44c6b0715249f1aed9f2de970eb67aa57b605191ca487d7647aeec7c08d104d7a610a64382e74511edc1ac101b76e668774971057642c060d09f689bdacbbb3ddc7b0191d907dfb765d518b139a34c9b803384bdfbcd6db
DEBUG: <<< ping from <Node(0x4d6b@176.28.19.157)>
DEBUG: >>> ponging <Node(0x4d6b@176.28.19.157)>
DEBUG: <<< pong from <Node(0x5c30@176.9.154.84)>
DEBUG: got expected pong with pingid 0xd1637a1651aaa68b33e6eb562c515768b4da39c9e30ca32a889fca36393916f14d6b5f5a2a94855297e430434a820aa4d32c882fb33e8402b344457a5d4430a1fa4822f1c3159e36be794c492bf8aa430febb0a24890ad187b475de9b37a3044
DEBUG: <<< ping from <Node(0x5c30@176.9.154.84)>
DEBUG: >>> ponging <Node(0x5c30@176.9.154.84)>
DEBUG: <<< pong from <Node(0x7e0d@136.243.88.194)>
DEBUG: got expected pong with pingid 0x81104fcb466260eed0ac65d124fef40b4019746de84e2e821a7d206e30e9e3795c30e1d3cc71132a03a9c0484bceb5a51276ce104b74d3fc37a1e6b8544da46787f163680f52f26a396ebdc439eddab81f18febf04b60c0a252f4ff44dae36ab
DEBUG: <<< pong from <Node(0x3afd@109.173.122.169)>
DEBUG: <<< ping from <Node(0x3afd@109.173.122.169)>
DEBUG: >>> ponging <Node(0x3afd@109.173.122.169)>
DEBUG: got expected pong with pingid 0x62cc09ca1f88463cdb0477d83d79f4b543823b2e96e9dfbfe94905c90873f4de7e0dac0b952ca998302bcb1b85f6fcfba2ef6f95cb7089c837c48c50684a94889895317e90843538f4eac1e3b8b39ba3c4b8531bff1e7fb181217cb5896bc869
DEBUG: <<< ping from <Node(0x7e0d@136.243.88.194)>
DEBUG: >>> ponging <Node(0x7e0d@136.243.88.194)>
DEBUG: got expected pong with pingid 0xa7c6abfbf2bfdac6326127a535dacb748d59ffdae1fe294546f2900dd934aba93afdcaf2de653027b39c71e99a2e6f28a60710639b11c35949acf6441eeaf6edf0a14506777d43c92b7a3ee97fa889451b71fe6ff0b2bced2c75f1e14708358c
DEBUG: <<< pong from <Node(0x1664@94.176.235.121)>
DEBUG: <<< ping from <Node(0x1664@94.176.235.121)>
DEBUG: >>> ponging <Node(0x1664@94.176.235.121)>
DEBUG: got expected ping from <Node(0x7e0d@136.243.88.194)>
DEBUG: bonding completed successfully with <Node(0x7e0d@136.243.88.194)>
DEBUG: <<< ping from <Node(0xf23b@169.50.227.54)>
DEBUG: >>> ponging <Node(0xf23b@169.50.227.54)>
DEBUG: got expected pong with pingid 0xe75571522f0ca538af39fddb12eb963198a49190cc41ef6cdbc5b3de42bc20db166478f9bf959b718212fbde4bbda90c5c68efeb5dcc0b37ed893874c3b912237c71f54c0df4b632315fc188a6ce792613bfa049868d1eea686007b22df88498
DEBUG: <<< ping from <Node(0x3cec@5.9.9.40)>
DEBUG: >>> ponging <Node(0x3cec@5.9.9.40)>
DEBUG: got expected ping from <Node(0xf23b@169.50.227.54)>
DEBUG: bonding completed successfully with <Node(0xf23b@169.50.227.54)>
DEBUG: got expected ping from <Node(0x3cec@5.9.9.40)>
DEBUG: bonding completed successfully with <Node(0x3cec@5.9.9.40)>
DEBUG: timed out waiting for neighbours response from <Node(0x43dd@146.148.112.168)>
DEBUG: got no candidates from <Node(0x43dd@146.148.112.168)>, returning
DEBUG: timed out waiting for neighbours response from <Node(0x4a48@139.59.111.210)>
DEBUG: got no candidates from <Node(0x4a48@139.59.111.210)>, returning
DEBUG: timed out waiting for pong with pingid 0xde0a4a361b84422e9ba2b776d666da191958b0e47a17b8ef7d7d373a30029cbedcb584dcf8d35a8166fb1f799a389da2ae7c3cf6e8ccdccdcbb622d2391f65556fc3f7dd25a6893bdc39d5c123df24a85d82a42036a68e9a66a7ad94f67e443b
DEBUG: bonding failed, didn't receive pong from <Node(0xdcb5@86.147.176.149)>
DEBUG: timed out waiting for pong with pingid 0x36041c6a70602f0bef96ca80aee7e8e4935eac004057d832484be25a4b1112c975f7ce705c80ef684f759e922e64757cfe3d572036879d1c3735c3e32b283e2399037949a94c49152606e4fe7c5f3da2c02cdb5f072eb79784894969cd179653
DEBUG: bonding failed, didn't receive pong from <Node(0x75f7@68.146.250.100)>
DEBUG: timed out waiting for ping from <Node(0x9039@108.39.204.189)>
DEBUG: bonding completed successfully with <Node(0x9039@108.39.204.189)>
DEBUG: timed out waiting for ping from <Node(0x0116@159.203.112.81)>
DEBUG: bonding completed successfully with <Node(0x0116@159.203.112.81)>
DEBUG: timed out waiting for ping from <Node(0x8e74@188.138.1.237)>
DEBUG: bonding completed successfully with <Node(0x8e74@188.138.1.237)>
DEBUG: timed out waiting for ping from <Node(0x799f@209.239.115.237)>
DEBUG: bonding completed successfully with <Node(0x799f@209.239.115.237)>
DEBUG: timed out waiting for ping from <Node(0xaa57@94.130.129.84)>
DEBUG: bonding completed successfully with <Node(0xaa57@94.130.129.84)>
DEBUG: timed out waiting for ping from <Node(0x690d@213.32.53.181)>
DEBUG: bonding completed successfully with <Node(0x690d@213.32.53.181)>
DEBUG: timed out waiting for ping from <Node(0x647a@84.29.40.212)>
DEBUG: bonding completed successfully with <Node(0x647a@84.29.40.212)>
DEBUG: timed out waiting for ping from <Node(0x4d6b@176.28.19.157)>
DEBUG: bonding completed successfully with <Node(0x4d6b@176.28.19.157)>
DEBUG: timed out waiting for ping from <Node(0x5c30@176.9.154.84)>
DEBUG: bonding completed successfully with <Node(0x5c30@176.9.154.84)>
DEBUG: timed out waiting for ping from <Node(0x3afd@109.173.122.169)>
DEBUG: bonding completed successfully with <Node(0x3afd@109.173.122.169)>
DEBUG: timed out waiting for ping from <Node(0x1664@94.176.235.121)>
DEBUG: bonding completed successfully with <Node(0x1664@94.176.235.121)>
DEBUG: bonded with 14 candidates
DEBUG: node lookup; querying [<Node(0xd8c3@35.189.249.117)>, <Node(0x1e1b@47.95.225.87)>, <Node(0x48cf@174.65.167.20)>]
DEBUG: >>> find_node to <Node(0xd8c3@35.189.249.117)>
DEBUG: >>> find_node to <Node(0x1e1b@47.95.225.87)>
DEBUG: >>> find_node to <Node(0x48cf@174.65.167.20)>
DEBUG: poll 888.988 ms took 165.273 ms: 1 events
DEBUG: <<< neighbours from <Node(0x48cf@174.65.167.20)>: [<Node(0x038f@211.54.97.10)>, <Node(0x4544@99.109.160.170)>, <Node(0x97e6@173.239.240.27)>, <Node(0x79a1@76.168.46.25)>, <Node(0x2df2@96.244.252.244)>, <Node(0xca6a@136.243.66.23)>, <Node(0x9fb1@73.9.139.106)>, <Node(0xe0dd@45.63.29.78)>, <Node(0x8c37@216.180.180.252)>, <Node(0xfc09@200.149.87.112)>, <Node(0xa3bd@121.69.48.155)>, <Node(0x9053@68.77.36.20)>]
DEBUG: poll 702.366 ms took 0.014 ms: 1 events
DEBUG: <<< neighbours from <Node(0x48cf@174.65.167.20)>: [<Node(0x3d83@121.14.103.224)>, <Node(0x219d@173.63.10.65)>, <Node(0xd92f@69.110.136.247)>, <Node(0x4d6b@176.28.19.157)>]
DEBUG: got expected neighbours response from <Node(0x48cf@174.65.167.20)>
DEBUG: got 13 new candidates
DEBUG: >>> pinging <Node(0x79a1@76.168.46.25)>
DEBUG: >>> pinging <Node(0xfc09@200.149.87.112)>
DEBUG: >>> pinging <Node(0x2df2@96.244.252.244)>
DEBUG: >>> pinging <Node(0x9fb1@73.9.139.106)>
DEBUG: >>> pinging <Node(0xa3bd@121.69.48.155)>
DEBUG: >>> pinging <Node(0xd92f@69.110.136.247)>
DEBUG: >>> pinging <Node(0xe0dd@45.63.29.78)>
DEBUG: >>> pinging <Node(0x4544@99.109.160.170)>
DEBUG: >>> pinging <Node(0x219d@173.63.10.65)>
DEBUG: >>> pinging <Node(0x8c37@216.180.180.252)>
DEBUG: >>> pinging <Node(0x3d83@121.14.103.224)>
DEBUG: >>> pinging <Node(0x97e6@173.239.240.27)>
DEBUG: >>> pinging <Node(0x038f@211.54.97.10)>
DEBUG: <<< neighbours from <Node(0x1e1b@47.95.225.87)>: [<Node(0xab61@82.217.36.111)>, <Node(0xc621@47.94.57.152)>, <Node(0x19dc@121.196.232.205)>, <Node(0x7cdc@217.163.65.254)>, <Node(0xa71d@167.114.232.209)>, <Node(0x80ab@103.36.139.135)>, <Node(0xdb9c@121.40.178.165)>, <Node(0xc363@172.104.252.26)>, <Node(0x736a@168.194.161.118)>, <Node(0x4446@119.23.44.241)>, <Node(0xf951@60.218.226.250)>, <Node(0x7296@176.100.8.107)>]
DEBUG: poll 601.200 ms took 0.015 ms: 1 events
DEBUG: <<< neighbours from <Node(0x1e1b@47.95.225.87)>: [<Node(0x9994@93.139.5.37)>, <Node(0x7e5f@178.71.227.181)>, <Node(0xa3af@5.196.83.147)>, <Node(0x1e2f@109.47.1.162)>]
DEBUG: <<< pong from <Node(0x2df2@96.244.252.244)>
DEBUG: got expected neighbours response from <Node(0x1e1b@47.95.225.87)>
DEBUG: got 16 new candidates
DEBUG: >>> pinging <Node(0xab61@82.217.36.111)>
DEBUG: >>> pinging <Node(0x19dc@121.196.232.205)>
DEBUG: >>> pinging <Node(0xf951@60.218.226.250)>
DEBUG: >>> pinging <Node(0x7296@176.100.8.107)>
DEBUG: >>> pinging <Node(0x736a@168.194.161.118)>
DEBUG: >>> pinging <Node(0x80ab@103.36.139.135)>
DEBUG: >>> pinging <Node(0x9994@93.139.5.37)>
DEBUG: >>> pinging <Node(0x7e5f@178.71.227.181)>
DEBUG: >>> pinging <Node(0xc363@172.104.252.26)>
DEBUG: >>> pinging <Node(0xdb9c@121.40.178.165)>
DEBUG: >>> pinging <Node(0xa3af@5.196.83.147)>
DEBUG: >>> pinging <Node(0xc621@47.94.57.152)>
DEBUG: >>> pinging <Node(0x1e2f@109.47.1.162)>
DEBUG: >>> pinging <Node(0xa71d@167.114.232.209)>
DEBUG: >>> pinging <Node(0x7cdc@217.163.65.254)>
DEBUG: >>> pinging <Node(0x4446@119.23.44.241)>
DEBUG: got expected pong with pingid 0x597d5b70ad61e0161f174b241670cc4a4fa3a459aa1098134bdfad37bc776eb32df2996a3d756505cfeb5ce957c576adeb60c37bd2fbaef7b68f611635bd09a369e0f887cfdf4abb73cc402d6e2d1786e227191a641d41489c5d491336213daf
DEBUG: poll 483.770 ms took 64.269 ms: 1 events
DEBUG: <<< pong from <Node(0xa3af@5.196.83.147)>
DEBUG: <<< ping from <Node(0xa3af@5.196.83.147)>
DEBUG: >>> ponging <Node(0xa3af@5.196.83.147)>
DEBUG: <<< pong from <Node(0x7296@176.100.8.107)>
DEBUG: got expected pong with pingid 0x6b73dd62ecdd6ceaef6afbfceaa11f4401a6125e0c1d96e87b092d5e0cbd6781a3af378c3d22408e5db98e7234e565e1c51e0e1213f4f422da91dcce6649d037d38e339b35bf126f726f31ee85fa154fb937dd132520698231dc96431d844636
DEBUG: <<< pong from <Node(0xc363@172.104.252.26)>
DEBUG: <<< pong from <Node(0x3d83@121.14.103.224)>
DEBUG: unexpected pong from <Node(0x3d83@121.14.103.224)> with pingid 0x4807b40f2587522de1fa0687a4561f95c7d2f87e2d38c30a6b36494ca559a6343d8371b2030d6bbb74b6388b3b694add9e3831fd0699cc3eb914d5b08d2f1f30f3f1edf2b41e2650165c82bfc8675e8f518866a34419a39651d8f5c2e7ea044b, probably came too late
DEBUG: got expected pong with pingid 0x777377c2a1d013e36ad3177f898577e10faa8b37df8cffad05fe6351c82a45317296b5e1b413058c4af07e50ccb11f5db5906447cb954a4c49a4ec3681d1b4123ad26c6dad6bb3bc3aaf4c24872716e0aefce4a3b202aa4a123ee323fc6bed28
DEBUG: <<< pong from <Node(0xa71d@167.114.232.209)>
DEBUG: unexpected pong from <Node(0xa71d@167.114.232.209)> with pingid 0xb1d948c56c572705f1cc5a756bb6112736a6ffa363efb56ccbf7d42270b44705a71df8184d635f0ce0703d7c2782477a9bc0f8ed15b95788939367d4e5ce65bd01e57de83c17c15ac9fd01ba6f32c3a3e0c6c8fb1ac26e728394dce73e096916, probably came too late
DEBUG: got expected pong with pingid 0x95a5ab42fc825c6cfbe9b6c2c329e182fc0917130830a0fbcfb3628db667f86fc363f6d28748b2fb6964b973916a788e618f61c549a3513acdedc5b58e011ee494b0f28445e03cec947c6e6103206f11aa7af05357a73e6d701ef1b3c30d4fc7
DEBUG: <<< pong from <Node(0x63a4@216.180.180.252)>
DEBUG: unexpected pong from <Node(0x63a4@216.180.180.252)> with pingid 0x98d11b1db35d465bf2fd2333ea2629430cf823ba0c0bd0ba3e4e930e8b2e35d163a4c30372eb8864d74b41e96827971126c638a711607339b17d7415ff15ade1450c021661f8e76b64204b0bb78f57ea9dee22322575ab7e7e4a14fa10475720, probably came too late
DEBUG: <<< ping from <Node(0xc363@172.104.252.26)>
DEBUG: >>> ponging <Node(0xc363@172.104.252.26)>
DEBUG: <<< pong from <Node(0x19dc@121.196.232.205)>
DEBUG: <<< ping from <Node(0x19dc@121.196.232.205)>
DEBUG: >>> ponging <Node(0x19dc@121.196.232.205)>
DEBUG: got expected ping from <Node(0xc363@172.104.252.26)>
DEBUG: bonding completed successfully with <Node(0xc363@172.104.252.26)>
DEBUG: <<< pong from <Node(0xc621@47.94.57.152)>
DEBUG: got expected pong with pingid 0xcc4f12ed590b4114ee7d5dab2a19d7c3deee7f6223327ff63379dbeb9b75606d19dc8ee5012be4888d8623a9bbd5624879cd25ef5d7baecde5188718094c56d6391b737ce9d468062c1e3048354e43caccbb34550ede5fc77921e99c40a17358
DEBUG: got expected pong with pingid 0xf006b13cc25fd48a5c9f334354b82f7df7c615aeeab2821146593dc9413b08e9c62145ef5302e886fc853c6782a354d419d03935b2a570335ef19c81f91316b346ed632fef8d53bdc64f6e6dab230ce225d851b404e6f9bdea46b08551f29242
DEBUG: poll 239.230 ms took 19.957 ms: 1 events
DEBUG: <<< pong from <Node(0x4446@119.23.44.241)>
DEBUG: <<< ping from <Node(0x4446@119.23.44.241)>
DEBUG: >>> ponging <Node(0x4446@119.23.44.241)>
DEBUG: <<< pong from <Node(0xdb9c@121.40.178.165)>
DEBUG: got expected pong with pingid 0x6671393c85df392569d59df470dbe87128dc02bfc368442f774a9a89b0e43cc1444682b4c9fdff475461f07dabb356bc137ce911ef0afc54f1151de7658cce0d1c930bd776910388f55fd9f3a8d3d8fcdb614d9b7310dc5c1f965322bec42a69
DEBUG: <<< ping from <Node(0xdb9c@121.40.178.165)>
DEBUG: >>> ponging <Node(0xdb9c@121.40.178.165)>
DEBUG: <<< pong from <Node(0x80ab@103.36.139.135)>
DEBUG: got expected pong with pingid 0x00b363510b1c0e0fece2d3259c03c647d47cb109ed593331a4c375f8972c4830db9c8f20669a089b844df0205308e948c6e2867a2b15097fe5fe38ba0951d896dedbda5c194c12a19de7d37c174a7c592c2707f533fefc6bbd2b0d90c691e7e5
DEBUG: <<< ping from <Node(0x80ab@103.36.139.135)>
DEBUG: >>> ponging <Node(0x80ab@103.36.139.135)>
DEBUG: <<< ping from <Node(0x63a4@216.180.180.252)>
DEBUG: >>> ponging <Node(0x63a4@216.180.180.252)>
DEBUG: got expected pong with pingid 0xe061701a0de235949fbede1f7db350ae719baf197cd3f21ba43b6f68cf3ddd0080abd10c924ab7862507f5dc5e184a42a16353ad8bb640b5f1469afa2a634e1a4165d7c3855e70ed83164953bda7572e803e3b75b9eaf7bca4ab442f29aecd63
DEBUG: timed out waiting for neighbours response from <Node(0xd8c3@35.189.249.117)>
DEBUG: got no candidates from <Node(0xd8c3@35.189.249.117)>, returning
DEBUG: poll 213.947 ms took 11.937 ms: 1 events
DEBUG: <<< ping from <Node(0x7296@176.100.8.107)>
DEBUG: >>> ponging <Node(0x7296@176.100.8.107)>
DEBUG: got expected ping from <Node(0x7296@176.100.8.107)>
DEBUG: bonding completed successfully with <Node(0x7296@176.100.8.107)>
DEBUG: timed out waiting for pong with pingid 0x7108f702df3748dd34a0305dfc4072486b1bf68398e841b6adeb1400b56f030f79a1fcb44c8b6f1ee7a516c6fc12dd8cb43f3cb50190a93d9437b9bb15a4a1e83fa2337704268d80bbb3efdd65706268be26afe668972885b1190c2c117598fb
DEBUG: bonding failed, didn't receive pong from <Node(0x79a1@76.168.46.25)>
DEBUG: timed out waiting for pong with pingid 0x0b9d069231481b44381c12b42cbd9e7bc297d2a71767af5f56e9ee3c5ef76599fc092d44838529510ef8b28c0354949341acba266ec0ae6d7322f2c741f3cf5cfc559d5c683bf0fbe1f11d52a9fa785c74526c416ff43893905b103fc5cee241
DEBUG: bonding failed, didn't receive pong from <Node(0xfc09@200.149.87.112)>
DEBUG: timed out waiting for pong with pingid 0x55b36f1e712ea9efffbd9e090cbe2f9cc059409fc378ea39f463ee340a5cc03d9fb1d1fa5e1757c0ed986623dbf3a509c8be7d67646533cd786330354bd3628491739e783c0b6e898c32ab44e8669e04dae235ada8d6515cd0bf556fed7d39da
DEBUG: bonding failed, didn't receive pong from <Node(0x9fb1@73.9.139.106)>
DEBUG: timed out waiting for pong with pingid 0xe4f0b069e90678337c6cbc8d2793998535af106a8f9de60259c3d98a3b51f960a3bdf2b5727684fa6fe8fd046fdac804fabf5558d87129d86134c5c280a22402c1f57eb359586b84d4434c8cdd08e9a95a6296d65a72b7ebb70272bc85ef9104
DEBUG: bonding failed, didn't receive pong from <Node(0xa3bd@121.69.48.155)>
DEBUG: timed out waiting for pong with pingid 0xa4f19ae01ac2f20f07b61bc14d5eec25f0e8f93a3054af6d29227538185bef94d92fc1caa7c0929306599db7bddaa2386fd139723cc85ff2bae4e2bb23df30c19cd0d30aef8a8543b8dfbeef78ecb0443e749aaf74a4da2e710c7a44742b99f6
DEBUG: bonding failed, didn't receive pong from <Node(0xd92f@69.110.136.247)>
DEBUG: timed out waiting for pong with pingid 0xb006f2c9b38cf2ca3fd8a20ff6e7150b34a2b3ad75cf3180c62e6fb88b67cf4fe0dd2383e75c63f1fa4f205c9bbea3aa0e9ad23fe1fedaa44f32e6f1d6f9a1ecfdc098c2f5ac2322b12999dc877f8c221b8a3e98965a98c7e2f89a4869e6704a
DEBUG: bonding failed, didn't receive pong from <Node(0xe0dd@45.63.29.78)>
DEBUG: timed out waiting for pong with pingid 0x8c8e7c6b8a437494783b2b5a88ce07b5a7cdf7ae04293f83c6f46b07e9a118a945443775647be21e193de62db5fb333d3422a1b915b1379a6869620a08689cfe7cb38221deaac8614cca62be61fdc42c4750cc5873f6996ea726e4fd94233170
DEBUG: bonding failed, didn't receive pong from <Node(0x4544@99.109.160.170)>
DEBUG: timed out waiting for pong with pingid 0x668d7d208e21bc2af22903f67ab6013391fd48aa3d8fdc0dec26a302bfe2fefb219d1346742568532744c18ba6fdb6f624dd8f58017c9a6202fab50eaab0c5aa80b71ca35b7f492d2a2345c5f0bfc4cea74ca097a11a0acfc03a2be5b322467c
DEBUG: bonding failed, didn't receive pong from <Node(0x219d@173.63.10.65)>
DEBUG: timed out waiting for pong with pingid 0x98d11b1db35d465bf2fd2333ea2629430cf823ba0c0bd0ba3e4e930e8b2e35d18c37364e8675d1c546a791472d8e1baea853974e6557627ec58ed880b74fa20477fb5fe98a79779141e8000c0be44f581290a33492f29e5b80dfc226c90c480b
DEBUG: bonding failed, didn't receive pong from <Node(0x8c37@216.180.180.252)>
DEBUG: timed out waiting for pong with pingid 0x675a3e7a4536ae608412ef92f994453c3dc1c137b853407d2fb5ae01952392d43d8371b2030d6bbb74b6388b3b694add9e3831fd0699cc3eb914d5b08d2f1f30f3f1edf2b41e2650165c82bfc8675e8f518866a34419a39651d8f5c2e7ea044b
DEBUG: bonding failed, didn't receive pong from <Node(0x3d83@121.14.103.224)>
DEBUG: timed out waiting for pong with pingid 0x9b43992d417b23ed273ceaeef3719c879dab0ebbaae4c2ed5a1762e10b52aa7497e685f6ef3d069c5c344c16eaf10ba9d3d2da81c1f579818b1d5d60fd82831c115639499699844b882076115d9c728816622e5552e571b1cf2f90e684d5bf0b
DEBUG: bonding failed, didn't receive pong from <Node(0x97e6@173.239.240.27)>
DEBUG: timed out waiting for pong with pingid 0xb9df65b8defbad7cfa46129da269c2a5498b8681d7a7a8b087ad5cbb5974fb13038f4aaa05d36b1ca337d013f4f011101280b3313a23dfd2a4191c4fe71e6c51cd3388cf20110987ee3fc94eaa7431cb46dc27acd23133874cf5200d8bc94faa
DEBUG: bonding failed, didn't receive pong from <Node(0x038f@211.54.97.10)>
DEBUG: timed out waiting for pong with pingid 0xfb3817bc81f615fff4da11df879589533435600d7f490efdd04b2759dbdf5939ab61065873ddfc74951688abcd2e1adc149bcb9e36aa4695e8b143cf2cb879e042b76ce653e590716a2c7575fa599733027b8248d68492da37dd4ac993c0ba4c
DEBUG: bonding failed, didn't receive pong from <Node(0xab61@82.217.36.111)>
DEBUG: timed out waiting for pong with pingid 0x5f20ebfb4c1df7fcfff74d3fcb74e348071d80872f9beb889fab72cbe3c759abf9510389dd94b95c1f7b389382db4073ff0bd1241e478c0c7fddb71c153943e404c4c0d58662237d0092013c32584ccd0da99575f3444493f3ae56f3ab425b24
DEBUG: bonding failed, didn't receive pong from <Node(0xf951@60.218.226.250)>
DEBUG: timed out waiting for pong with pingid 0xbcab622133be4e63197ee3063dfed1733b48e1339ff63cca225597e688fc92ce736a1abb7649bce175f7608cb2ac4342b8544856392ac28713918e068d0b517e2694df18b624d57b9cb62972d53a7c12dfd04a24b7ce12d734c2f3754992c8b9
DEBUG: bonding failed, didn't receive pong from <Node(0x736a@168.194.161.118)>
DEBUG: timed out waiting for pong with pingid 0x1f8e12087fcf2465a47cb97c5b86fa999d751a1b2491cab65e58b3c182f4a88c99941dba5e7dce5a313941d32791d815467d4c157ab1a6ab46f7f79e146f00811e962d27fc3e37b290c48ec0ed97213ed8ffbf347ebcc64e13eb5115fc08f446
DEBUG: bonding failed, didn't receive pong from <Node(0x9994@93.139.5.37)>
DEBUG: timed out waiting for pong with pingid 0x85c8458228fa5d68bcfe403e8c5922dabcd29c65aa98df62ae9d14a067b507497e5f87ea8bfb52ab3222bad20db4af4e90522f642f8930f79c11d7cd0b76285598eb0d67696cf3e3c5037aa3f624b39b8d881351bd0c0eb748a6bda0bbf96224
DEBUG: bonding failed, didn't receive pong from <Node(0x7e5f@178.71.227.181)>
DEBUG: timed out waiting for pong with pingid 0xcdbfe4f7a3fb5b85f72689173e839a30c486987b0dfd7d20da9b01cf408299671e2fa55f69ef33c750ba1a0648a90d5eee47a3674ed150a2b9f48c5c75b2ae86df4a751ebc3c862ffb8f8321b4789018ba1b2a3bbad40ca5eb32f6efbb5d8a30
DEBUG: bonding failed, didn't receive pong from <Node(0x1e2f@109.47.1.162)>
DEBUG: timed out waiting for pong with pingid 0x9ba7976c7664eb36708b3721b2ecc9b09c65a36648c66d3848a6c1b31548846fa71df8184d635f0ce0703d7c2782477a9bc0f8ed15b95788939367d4e5ce65bd01e57de83c17c15ac9fd01ba6f32c3a3e0c6c8fb1ac26e728394dce73e096916
DEBUG: bonding failed, didn't receive pong from <Node(0xa71d@167.114.232.209)>
DEBUG: timed out waiting for pong with pingid 0x1440e4125a5d5a59f3e008af50f655e9f1d3e1d4a3bc606f6f26ebfb7348c86b7cdc7f102f6df80fdf5288deb3090a6b8b680bba02716ce3ded384fa3cdaea4c3cf05fef2f3e448c9e7d539d7a55a094e9f25520b6f81cee642f276cb8ea5c61
DEBUG: bonding failed, didn't receive pong from <Node(0x7cdc@217.163.65.254)>
DEBUG: timed out waiting for ping from <Node(0x2df2@96.244.252.244)>
DEBUG: bonding completed successfully with <Node(0x2df2@96.244.252.244)>
DEBUG: bonded with 1 candidates
DEBUG: timed out waiting for ping from <Node(0xa3af@5.196.83.147)>
DEBUG: bonding completed successfully with <Node(0xa3af@5.196.83.147)>
DEBUG: timed out waiting for ping from <Node(0x19dc@121.196.232.205)>
DEBUG: bonding completed successfully with <Node(0x19dc@121.196.232.205)>
DEBUG: timed out waiting for ping from <Node(0xc621@47.94.57.152)>
DEBUG: bonding completed successfully with <Node(0xc621@47.94.57.152)>
DEBUG: timed out waiting for ping from <Node(0x4446@119.23.44.241)>
DEBUG: bonding completed successfully with <Node(0x4446@119.23.44.241)>
DEBUG: timed out waiting for ping from <Node(0xdb9c@121.40.178.165)>
DEBUG: bonding completed successfully with <Node(0xdb9c@121.40.178.165)>
DEBUG: timed out waiting for ping from <Node(0x80ab@103.36.139.135)>
DEBUG: bonding completed successfully with <Node(0x80ab@103.36.139.135)>
DEBUG: bonded with 8 candidates
DEBUG: node lookup; querying [<Node(0x0dbf@210.55.87.47)>, <Node(0x4b57@13.64.146.159)>, <Node(0x799f@209.239.115.237)>]
DEBUG: >>> find_node to <Node(0x0dbf@210.55.87.47)>
DEBUG: >>> find_node to <Node(0x799f@209.239.115.237)>
DEBUG: >>> find_node to <Node(0x4b57@13.64.146.159)>
DEBUG: poll 889.130 ms took 29.909 ms: 1 events
DEBUG: <<< neighbours from <Node(0x799f@209.239.115.237)>: [<Node(0x21e6@93.193.94.127)>, <Node(0x8e74@188.138.1.237)>, <Node(0x65b4@139.162.87.55)>, <Node(0x195c@46.101.143.7)>, <Node(0x2c2f@66.147.230.39)>, <Node(0xdb65@163.172.41.198)>, <Node(0x7f55@82.68.93.54)>, <Node(0xe76f@52.71.147.64)>, <Node(0x592d@14.202.226.2)>, <Node(0x2fec@145.239.144.185)>, <Node(0x83c3@165.227.214.75)>, <Node(0xca6a@136.243.66.23)>]
DEBUG: poll 837.830 ms took 0.017 ms: 1 events
DEBUG: <<< neighbours from <Node(0x799f@209.239.115.237)>: [<Node(0x4f40@136.243.173.151)>, <Node(0xfafe@86.86.183.108)>, <Node(0x5c30@176.9.154.84)>, <Node(0x2b29@75.141.166.249)>]
DEBUG: got expected neighbours response from <Node(0x799f@209.239.115.237)>
DEBUG: got 12 new candidates
DEBUG: >>> pinging <Node(0x7f55@82.68.93.54)>
DEBUG: >>> pinging <Node(0x2b29@75.141.166.249)>
DEBUG: >>> pinging <Node(0x21e6@93.193.94.127)>
DEBUG: >>> pinging <Node(0xfafe@86.86.183.108)>
DEBUG: >>> pinging <Node(0x2fec@145.239.144.185)>
DEBUG: >>> pinging <Node(0x2c2f@66.147.230.39)>
DEBUG: >>> pinging <Node(0xdb65@163.172.41.198)>
DEBUG: >>> pinging <Node(0x592d@14.202.226.2)>
DEBUG: >>> pinging <Node(0xe76f@52.71.147.64)>
DEBUG: >>> pinging <Node(0x195c@46.101.143.7)>
DEBUG: >>> pinging <Node(0x4f40@136.243.173.151)>
DEBUG: >>> pinging <Node(0x65b4@139.162.87.55)>
DEBUG: <<< neighbours from <Node(0x4b57@13.64.146.159)>: [<Node(0x9039@108.39.204.189)>, <Node(0x6357@103.235.247.144)>, <Node(0xe806@212.8.242.197)>, <Node(0x799f@209.239.115.237)>, <Node(0x690d@213.32.53.181)>, <Node(0x54f0@149.56.245.193)>, <Node(0x3ce6@64.46.2.236)>, <Node(0x5a8a@51.15.60.23)>, <Node(0x70cf@107.155.29.148)>, <Node(0x90b0@144.217.66.227)>, <Node(0xdcb5@86.147.176.149)>, <Node(0x2207@34.205.23.63)>]
DEBUG: poll 740.278 ms took 0.026 ms: 1 events
DEBUG: <<< neighbours from <Node(0x4b57@13.64.146.159)>: [<Node(0xd218@104.131.6.141)>, <Node(0x6bdd@94.130.129.84)>, <Node(0x1664@94.176.235.121)>, <Node(0x4d6b@176.28.19.157)>]
DEBUG: <<< pong from <Node(0x2c2f@66.147.230.39)>
DEBUG: got expected neighbours response from <Node(0x4b57@13.64.146.159)>
DEBUG: got 10 new candidates
DEBUG: >>> pinging <Node(0x6357@103.235.247.144)>
DEBUG: >>> pinging <Node(0xe806@212.8.242.197)>
DEBUG: >>> pinging <Node(0x2207@34.205.23.63)>
DEBUG: >>> pinging <Node(0x90b0@144.217.66.227)>
DEBUG: >>> pinging <Node(0x3ce6@64.46.2.236)>
DEBUG: >>> pinging <Node(0xd218@104.131.6.141)>
DEBUG: >>> pinging <Node(0x54f0@149.56.245.193)>
DEBUG: >>> pinging <Node(0x5a8a@51.15.60.23)>
DEBUG: >>> pinging <Node(0x6bdd@94.130.129.84)>
DEBUG: >>> pinging <Node(0x70cf@107.155.29.148)>
DEBUG: got expected pong with pingid 0xedd49c3023f4d8d537a5b1f0fc6d3948dd860ec5f403eb7226aa742d8d33a5382c2fabac9ef114382168ce63cc24d0038c3e6ccffab964de33ba8365fed49071975bda418a97597bf51079d60049af44915ceada399ffbb1d6e0cecf6bf96775
DEBUG: <<< pong from <Node(0x2fec@145.239.144.185)>
DEBUG: <<< pong from <Node(0xfafe@86.86.183.108)>
DEBUG: <<< pong from <Node(0xdb65@163.172.41.198)>
DEBUG: got expected pong with pingid 0x0fc34ed45f5a56b260bfefd08415514caa8ac02d89cbb343a4ea46c98c4d25712fec45e0952775ce19ab5a512f08ea0db80602fc63c34963dc031f232bfa1137f5a136a47f7c09b8fe56012d04920fa455985fd04613f3682acf982acb4a6d43
DEBUG: <<< pong from <Node(0x195c@46.101.143.7)>
DEBUG: got expected pong with pingid 0x60da537037842bbe4d08e5e76e5e03126d99e4bdfb5a8e941fd6527d0425e2d7fafe1d191cb604519796b27d89ccb2eea3b83a66e3ae96a148f364c9e34641596133ded2b9d5d721397a647e12a89fc7dd39c0243db0e197f1638409c899dc30
DEBUG: <<< pong from <Node(0x2207@34.205.23.63)>
DEBUG: got expected pong with pingid 0xf990effb638dbfb251b205030af1b30cd41896843f6272c28361f3b5075cee59db654724bb02ebe97e325e73496ce380cbca86813ad24d36c17638fdbcf7f23bd72e9f4011dc21dd4bd4fe71ce9fc6a7a8ddb29f5cb0857ae4b92e2c966d028f
DEBUG: <<< ping from <Node(0x2207@34.205.23.63)>
DEBUG: >>> ponging <Node(0x2207@34.205.23.63)>
DEBUG: got expected pong with pingid 0xed3b891c3f2e8bb5df03d2a54d05417a6dc66f97655b504cf8bc5ea413e52f22195cc1e73b6daed129e634e26a2e9e03b454cf77329d5482c7a8ba974e68574a8c65014d26b2fd95c9c92429ce7bdfa4a561486a7eb3e928e1dbe1f20727f01c
DEBUG: <<< pong from <Node(0x90b0@144.217.66.227)>
DEBUG: got expected pong with pingid 0x2f5a00702f5b0d4385afd27b3d336f17fbbfc67756d6bbd45ae4c1f098ab15a82207677bf133ba42e328e198caba1544021d95e0992971cad4738b70e106d7d2ce8f2c02559bac9ff52541fdc28739f953a993e0c34d0361019c6d9a0b582ee2
DEBUG: <<< ping from <Node(0x90b0@144.217.66.227)>
DEBUG: >>> ponging <Node(0x90b0@144.217.66.227)>
DEBUG: <<< neighbours from <Node(0x0dbf@210.55.87.47)>: [<Node(0x52f2@14.52.209.128)>, <Node(0xaef9@45.47.229.110)>, <Node(0xd0aa@41.96.160.194)>, <Node(0xa9de@213.197.164.242)>, <Node(0xf48a@93.115.29.168)>, <Node(0x4d91@46.105.115.90)>, <Node(0xee10@67.52.120.140)>, <Node(0xffb6@159.203.245.185)>, <Node(0xd2e5@118.178.182.73)>, <Node(0xebc7@75.100.81.216)>, <Node(0x0af9@52.59.25.31)>, <Node(0x7fd5@210.180.118.188)>]
DEBUG: got expected pong with pingid 0xe580cdb04ba581b5262239054ed4731bc82a63f540591acc7da1c1670d13305590b050ee5b3b9d373dae06d65136fa466f04c035cc6b80e7a6eeee47f741f0b543a3db02200a4f53b61a714d6772c05e6c0afbec23b19087606d0ea1a86abe22
DEBUG: <<< neighbours from <Node(0x0dbf@210.55.87.47)>: [<Node(0x1664@94.176.235.121)>, <Node(0x4d6b@176.28.19.157)>, <Node(0x628b@104.211.181.7)>, <Node(0x91e8@95.232.107.91)>]
DEBUG: <<< pong from <Node(0x4f40@136.243.173.151)>
DEBUG: unexpected pong from <Node(0x4f40@136.243.173.151)> with pingid 0xd4d83f5d6bd2e57a86b483de3d66b8992f9348f9f97b37139ec3b8fe741acafc4f40105e9e1587634a88113db8193c87cba0e99cbba58bc7c342ea7680cd2a57bd6153292f98e9d34a2375d3198eeb0a08aeb14d9f6f3a97f7808e2abce7531f, probably came too late
DEBUG: <<< pong from <Node(0xd218@104.131.6.141)>
DEBUG: got expected neighbours response from <Node(0x0dbf@210.55.87.47)>
DEBUG: got 13 new candidates
DEBUG: <<< ping from <Node(0xd218@104.131.6.141)>
DEBUG: >>> ponging <Node(0xd218@104.131.6.141)>
DEBUG: >>> pinging <Node(0xa9de@213.197.164.242)>
DEBUG: >>> pinging <Node(0xffb6@159.203.245.185)>
DEBUG: >>> pinging <Node(0x628b@104.211.181.7)>
DEBUG: >>> pinging <Node(0xebc7@75.100.81.216)>
DEBUG: >>> pinging <Node(0xaef9@45.47.229.110)>
DEBUG: >>> pinging <Node(0x91e8@95.232.107.91)>
DEBUG: >>> pinging <Node(0x0af9@52.59.25.31)>
DEBUG: >>> pinging <Node(0xf48a@93.115.29.168)>
DEBUG: >>> pinging <Node(0xee10@67.52.120.140)>
DEBUG: >>> pinging <Node(0xd0aa@41.96.160.194)>
DEBUG: >>> pinging <Node(0x4d91@46.105.115.90)>
DEBUG: >>> pinging <Node(0xd2e5@118.178.182.73)>
DEBUG: >>> pinging <Node(0x52f2@14.52.209.128)>
DEBUG: <<< pong from <Node(0x54f0@149.56.245.193)>
DEBUG: got expected pong with pingid 0x5a02760e1287879b8ef2e31da4b95c0a7f427aa7a7beb87fcd4aaf97e2dbcbc7d2187ee33c1a252ae0c25e082791ea494bcfcb094b85803415020257442f7ad2c26b775512dc99df7769a0d0cf64b04189b9f9b6b42ccd6f728cb8483d6f9c1c
DEBUG: <<< ping from <Node(0x54f0@149.56.245.193)>
DEBUG: >>> ponging <Node(0x54f0@149.56.245.193)>
DEBUG: <<< pong from <Node(0xe806@212.8.242.197)>
DEBUG: got expected pong with pingid 0x7434ba0a8d7d6b29e4a46caf5261c35168b783aebd4af2880c9ac04891d48e5554f087fee58fd74d674cd8b3ec91b15c51f328a3bcb3e20da7ae23b1d567bc7ddcdb66dca99f5c50e37e493087c81afd2e7c80ce5d7b710784e3894580fa91df
DEBUG: <<< pong from <Node(0x5a8a@51.15.60.23)>
DEBUG: <<< pong from <Node(0x65b4@139.162.87.55)>
DEBUG: unexpected pong from <Node(0x65b4@139.162.87.55)> with pingid 0xffbddb8b54925afcee5fa33f50b856c81aced41a0b0b210f22f881309f87997565b464ae7961d9adcfc4e69143bb037966f7bdb872a497c6e5e7453c4a44884ed9d0f7ab6446c181c1f7b9ff6df1eead7d1b7ac082484d71cac57732d8b6c8d2, probably came too late
DEBUG: got expected pong with pingid 0x6abb7ceebd2500e7402bd540c21b13576527198ccf2c69200666756b6c764db5e80656a0ab043d18ec74dda02e5de56342c1b8308b1831a4d4d6bb5cb6c748fc4902e240bfcdbfc9e56064442b832b628c483c8f6f45f25578546ff932e3f631
DEBUG: <<< ping from <Node(0x5a8a@51.15.60.23)>
DEBUG: >>> ponging <Node(0x5a8a@51.15.60.23)>
DEBUG: got expected pong with pingid 0x932783dc42bfd2c5701da93c9c05593f87a10200d1d47b38c9fcc8d31e85513c5a8aa14352e8f6fbbb04a0f5b5cb98204c38ce5696d55cf3c4682f6ead631182c5b732f9c377b0562d42bff8796387778edd9bf45ade80fb362ebce25d6b33d8
DEBUG: <<< pong from <Node(0x6bdd@94.130.129.84)>
DEBUG: <<< ping from <Node(0x6bdd@94.130.129.84)>
DEBUG: >>> ponging <Node(0x6bdd@94.130.129.84)>
DEBUG: <<< pong from <Node(0x592d@14.202.226.2)>
DEBUG: got expected pong with pingid 0x254962acecc998ab3e972684d0c871a820f3a694dc717d69db3c30d1cd4687536bdd516922fd6bb9dee9c67a8086e8d4a1ff152708dc4719a986e6a5b2f2dace788c5e3f5122489ca41ef3ec5bab678bfe788a9d3219599be90786d44ec2afe1
DEBUG: <<< ping from <Node(0x592d@14.202.226.2)>
DEBUG: >>> ponging <Node(0x592d@14.202.226.2)>
DEBUG: <<< pong from <Node(0x6357@103.235.247.144)>
DEBUG: got expected pong with pingid 0x2690ceb24eac73198f8f918c4d29e299c0242b04de6cc322c99c22a67817344a592d6d3a14e0cdc2f8311055c4bd0c390397de5c468366e9d6207d2e5b0d1e28fc173916b5ec13df55f3b0aa3806662383081630d76d4426a91b23dceeadf1cc
DEBUG: <<< pong from <Node(0xe76f@52.71.147.64)>
DEBUG: unexpected pong from <Node(0xe76f@52.71.147.64)> with pingid 0xe42b1d8b08c4f61cd56fb7d1218879ce3d6c8f297508ff16b173959e8e178ebfe76f0f36551fd018b07eec35cede991adaad67bf8db5f079af9314e72f2904f050b3d67e18911807d80ccf94b215f306c5caffb584c0aa602080f25a2c7403fb, probably came too late
DEBUG: <<< pong from <Node(0x70cf@107.155.29.148)>
DEBUG: got expected pong with pingid 0x5b7ee5f6fd5c9c07e4604347a3f048e099b96ff268aff2b275c96ab6f4c7da3d635731e9390d02e4f2fc8efa58c754db169cb12318d87d1ba2b4c7a1c8e4bfcaa2590dba2c59d8964acb721c6a61ddcb984203895f4604fe628e374b9b7df44d
DEBUG: <<< ping from <Node(0x70cf@107.155.29.148)>
DEBUG: >>> ponging <Node(0x70cf@107.155.29.148)>
DEBUG: <<< pong from <Node(0x2b29@75.141.166.249)>
DEBUG: got expected pong with pingid 0xf3446bae5963a59737f1ee3b9a71b1a070579d993f384a4f8286e4fc42d9be8a70cfd748def42f5b6b26f5d354c00d15b9f755cece735dc69e6417c76e45b7bc32660788cb5ec9a42f0792b636d8ecb686ce29e7cedd89e856d35df59e3d40f2
DEBUG: <<< pong from <Node(0xaef9@45.47.229.110)>
DEBUG: <<< ping from <Node(0xaef9@45.47.229.110)>
DEBUG: >>> ponging <Node(0xaef9@45.47.229.110)>
DEBUG: got expected pong with pingid 0xbc2a3f2d079cd3ef90e6a906cae21057011a165914de55c3fd1b0209b3e23d6b2b29992785d54072a0a3bf46e46d7e1d6a062fa4417fb94f3416c85e07e7641b39ef18d2af31c35f67bd8a77596a7ffb86615818b942a91b5f085f3c8a62f60d
DEBUG: <<< pong from <Node(0xffb6@159.203.245.185)>
DEBUG: got expected pong with pingid 0x17a0515bc871306ea5972ae537fe127d33c47a6047c84cf31b51c60e2637c80faef9b8ce2bf02104ff98a85d957ad42476e60a7633581e508a4a717a0507e782eefbeef7ee3d19454f72f0e59a145353e460652d2167941004c90d9c0c898565
DEBUG: <<< ping from <Node(0xffb6@159.203.245.185)>
DEBUG: >>> ponging <Node(0xffb6@159.203.245.185)>
DEBUG: <<< pong from <Node(0x0af9@52.59.25.31)>
DEBUG: got expected pong with pingid 0xe909cd4668d8a61ba1c6a21f92175e3f3ff293921771345f6db9b1842643f87effb60c18ebd6427669177f1f44b97dfda5075ecd1ea0e8f474bfcd3707deda7abd222f1caca7c1c4e2f809bd26d18d3ea315673279504e5562aa2e296d1b7554
DEBUG: <<< ping from <Node(0x0af9@52.59.25.31)>
DEBUG: >>> ponging <Node(0x0af9@52.59.25.31)>
DEBUG: <<< pong from <Node(0x4d91@46.105.115.90)>
DEBUG: got expected pong with pingid 0x12fd4c901dcd4a0e765ba80c6093d2d18995cc4da1e70fd7fb0dc669cf6099490af9713df38271f850851d152592ff72b42591677cac6984eb988956556f2a4337c27ca41957263572b2345ca2fd501c97f5b3ff963e624c386b4f1ee16e6b9b
DEBUG: <<< ping from <Node(0x4d91@46.105.115.90)>
DEBUG: >>> ponging <Node(0x4d91@46.105.115.90)>
DEBUG: <<< pong from <Node(0xf48a@93.115.29.168)>
DEBUG: got expected pong with pingid 0xe4f09803ecbdf35ae93cec78d29d1cbd132cd0f0f3d7ca8d6586aa5c72973cef4d91255078230bd31882828f2608ce8528bdb6b3954051c9d0b5a16171e745995984fb791769e5512e9acaa4c1ca294a4813ea7557ea70d2a3a26e717d29a595
DEBUG: <<< ping from <Node(0xf48a@93.115.29.168)>
DEBUG: >>> ponging <Node(0xf48a@93.115.29.168)>
DEBUG: <<< pong from <Node(0xd0aa@41.96.160.194)>
DEBUG: got expected pong with pingid 0xe6cb7edd137ef7fe23152dd38d3f789661df9bd59522b3e248bb483b7c96373df48ae0d4e844e1d4fd7342925b50fb158589fe02cfd2f96f18341fd3abcbb9a0f05cb4828c36611b82091ee43e1712f085e0a1d46a39bc7b08f0efba154178a5
DEBUG: <<< ping from <Node(0xd0aa@41.96.160.194)>
DEBUG: >>> ponging <Node(0xd0aa@41.96.160.194)>
DEBUG: <<< pong from <Node(0x628b@104.211.181.7)>
DEBUG: got expected pong with pingid 0x276fc6d76002ee75fbdab791cc7e79e070d25b7b302f86f93faf8841acc160f9d0aa34398131245c15e7c68b735c1600f7a1c7c8197eb42d55d184b1202af098950d2ebf1f3eeaf483fe3965e7da9698d71d3002c392d61adb03785398f6b9d8
DEBUG: <<< ping from <Node(0x628b@104.211.181.7)>
DEBUG: >>> ponging <Node(0x628b@104.211.181.7)>
DEBUG: <<< pong from <Node(0xd2e5@118.178.182.73)>
DEBUG: got expected pong with pingid 0x0cd24f91cf435a71ff3e13315c148b24592ca25a85289343a56a4e593c0ff0d4628bd4e744c93d2dc5bed74696b626d48b50350e3a44e21e409d888ac32f9e03e658f014cafcc376f5d948edd16e7bd2483feb83f7501862b9f1bdf07eec846f
DEBUG: timed out waiting for pong with pingid 0xf340c8792026022124c9124f75c610423c44d5bf5c1d798f203aa3bf0e08bad37f554a15f9ffa22f25012a1f0cc37b148bc6ae16693997fdf023d4704b90050b48c78a6da0075b7ec3d6e1a0ea8a5f5d67a3cb1a4e0855738fcbfc8a0a1385f6
DEBUG: bonding failed, didn't receive pong from <Node(0x7f55@82.68.93.54)>
DEBUG: <<< ping from <Node(0xd2e5@118.178.182.73)>
DEBUG: >>> ponging <Node(0xd2e5@118.178.182.73)>
DEBUG: timed out waiting for pong with pingid 0xad3a56ed639fac98eba19694f0bf8e5edf1cfbbd913510a398a7c8d6f483453121e63cc9f1413e30c511113ae17b5a0181e3a918010eda6286be349e98b3f39ca8e0accd65dcc2b53d192a8db7200686d4107113e6ea1c8bd2b61e3aacaeb224
DEBUG: bonding failed, didn't receive pong from <Node(0x21e6@93.193.94.127)>
DEBUG: got expected pong with pingid 0xddb6d66ddddd66705674ddb4f0d6ea04f9ac88600bb99e921c83170b71b585d6d2e5611bf4a62135463be7cc2503f8f48d86908b02d25d54d2050d221a3c1a37a597efa959129a928b3b1f645072adfb116e0f3a99cdb8cccf814dee770715c5
DEBUG: timed out waiting for pong with pingid 0x0d2b45d44b1e2d3543527bb9ec7fcb380adcf75d919aa02e98fa0bab3e4976d7e76f0f36551fd018b07eec35cede991adaad67bf8db5f079af9314e72f2904f050b3d67e18911807d80ccf94b215f306c5caffb584c0aa602080f25a2c7403fb
DEBUG: bonding failed, didn't receive pong from <Node(0xe76f@52.71.147.64)>
DEBUG: timed out waiting for pong with pingid 0x01fd51c407fd6e456b7ada1e7046e4c47c9f79be2896968b43507c29fcff94314f40105e9e1587634a88113db8193c87cba0e99cbba58bc7c342ea7680cd2a57bd6153292f98e9d34a2375d3198eeb0a08aeb14d9f6f3a97f7808e2abce7531f
DEBUG: bonding failed, didn't receive pong from <Node(0x4f40@136.243.173.151)>
DEBUG: timed out waiting for pong with pingid 0xc9836c080302ea1c581ca9c7851942e8fd252db5685294aeec3e5fd70bdf357d65b464ae7961d9adcfc4e69143bb037966f7bdb872a497c6e5e7453c4a44884ed9d0f7ab6446c181c1f7b9ff6df1eead7d1b7ac082484d71cac57732d8b6c8d2
DEBUG: bonding failed, didn't receive pong from <Node(0x65b4@139.162.87.55)>
DEBUG: timed out waiting for pong with pingid 0x664b5cf6686494cc7050ff85612eea46973180116908971bb8a93dc2751dc2853ce6173b170956e95fb554b390a461f7f2b212009cf578a9330bad942f7fb4c1ad0c6892fa4c26110764a10f74e8949fa11c27fa1f05365a8e11e88ab5a73565
DEBUG: bonding failed, didn't receive pong from <Node(0x3ce6@64.46.2.236)>
DEBUG: timed out waiting for ping from <Node(0x2c2f@66.147.230.39)>
DEBUG: bonding completed successfully with <Node(0x2c2f@66.147.230.39)>
DEBUG: timed out waiting for ping from <Node(0x2fec@145.239.144.185)>
DEBUG: bonding completed successfully with <Node(0x2fec@145.239.144.185)>
DEBUG: timed out waiting for ping from <Node(0xfafe@86.86.183.108)>
DEBUG: bonding completed successfully with <Node(0xfafe@86.86.183.108)>
DEBUG: timed out waiting for ping from <Node(0xdb65@163.172.41.198)>
DEBUG: bonding completed successfully with <Node(0xdb65@163.172.41.198)>
DEBUG: timed out waiting for ping from <Node(0x195c@46.101.143.7)>
DEBUG: bonding completed successfully with <Node(0x195c@46.101.143.7)>
DEBUG: timed out waiting for ping from <Node(0x2207@34.205.23.63)>
DEBUG: bonding completed successfully with <Node(0x2207@34.205.23.63)>
DEBUG: timed out waiting for ping from <Node(0x90b0@144.217.66.227)>
DEBUG: bonding completed successfully with <Node(0x90b0@144.217.66.227)>
DEBUG: timed out waiting for pong with pingid 0x3b8b17636644578c01754803bb0ba97d9052c667ebe39f1f499dc1ea64768c8fa9de647d3c89c68c6e1d4b42b6239f20ee0a95eac38755dd7528fde9f64f46ed150e9bc88097ac9ad2addaf65ebcebd0bcba63807f6fef3de6c84bebe9699594
DEBUG: bonding failed, didn't receive pong from <Node(0xa9de@213.197.164.242)>
DEBUG: timed out waiting for pong with pingid 0xc0edb274815313b0d37e1c6b0fd25d3e87ccf2e88ccf45c59619055980dd18afebc70c2a4c3934dc655fcb416958b85ae8fa4429972f93d6c0c631971e5dd67af69512271b906c3562fff223193b936f845680fdb691cd78ec2f22554a83669b
DEBUG: bonding failed, didn't receive pong from <Node(0xebc7@75.100.81.216)>
DEBUG: timed out waiting for pong with pingid 0x816e952e1e8c308f9d76ee9088a08e6c92b0a4f40b629854b34c2b10412d6c6491e86e0aad22f1f6f5f09bd01a073e2fd709a2021bc46e4ab72686c429aac683a83cd01e49eb94a864d9ad78a0f3e4754a4adeaf10a43e9e3c007fd6fb0efe38
DEBUG: bonding failed, didn't receive pong from <Node(0x91e8@95.232.107.91)>
DEBUG: timed out waiting for pong with pingid 0xe958bd0a6129a440a8fb9edaad2981ede37f253a11329757e0a6cfe506732090ee10509c6c99f0418912245c5e1e1527472029a080887c63052e90b6ca5d4fed3d12df18ab0b27e7d65b74ff37dd60e3312cc4148e81ee18d5858a8fb0fd6012
DEBUG: bonding failed, didn't receive pong from <Node(0xee10@67.52.120.140)>
DEBUG: timed out waiting for pong with pingid 0xc71552287ad06c70465adecff857718ecfe34d9bd3ddc9c196b9eb4b9c98be2c52f263ff8c2397ed7b2d7cdf76aeb279778bee86346ee49b7c8664448a6e91b838d81de1bf53a8182fbd9f345bef4f1e83f3ce8cbe4a14ca6deb43e4246eceb7
DEBUG: bonding failed, didn't receive pong from <Node(0x52f2@14.52.209.128)>
DEBUG: timed out waiting for ping from <Node(0xd218@104.131.6.141)>
DEBUG: bonding completed successfully with <Node(0xd218@104.131.6.141)>
DEBUG: timed out waiting for ping from <Node(0x54f0@149.56.245.193)>
DEBUG: bonding completed successfully with <Node(0x54f0@149.56.245.193)>
DEBUG: timed out waiting for ping from <Node(0xe806@212.8.242.197)>
DEBUG: bonding completed successfully with <Node(0xe806@212.8.242.197)>
DEBUG: timed out waiting for ping from <Node(0x5a8a@51.15.60.23)>
DEBUG: bonding completed successfully with <Node(0x5a8a@51.15.60.23)>
DEBUG: timed out waiting for ping from <Node(0x6bdd@94.130.129.84)>
DEBUG: bonding completed successfully with <Node(0x6bdd@94.130.129.84)>
DEBUG: timed out waiting for ping from <Node(0x592d@14.202.226.2)>
DEBUG: bonding completed successfully with <Node(0x592d@14.202.226.2)>
DEBUG: timed out waiting for ping from <Node(0x6357@103.235.247.144)>
DEBUG: bonding completed successfully with <Node(0x6357@103.235.247.144)>
DEBUG: timed out waiting for ping from <Node(0x70cf@107.155.29.148)>
DEBUG: bonding completed successfully with <Node(0x70cf@107.155.29.148)>
DEBUG: bonded with 9 candidates
DEBUG: timed out waiting for ping from <Node(0x2b29@75.141.166.249)>
DEBUG: bonding completed successfully with <Node(0x2b29@75.141.166.249)>
DEBUG: bonded with 7 candidates
DEBUG: timed out waiting for ping from <Node(0xaef9@45.47.229.110)>
DEBUG: bonding completed successfully with <Node(0xaef9@45.47.229.110)>
DEBUG: timed out waiting for ping from <Node(0xffb6@159.203.245.185)>
DEBUG: bonding completed successfully with <Node(0xffb6@159.203.245.185)>
DEBUG: timed out waiting for ping from <Node(0x0af9@52.59.25.31)>
DEBUG: bonding completed successfully with <Node(0x0af9@52.59.25.31)>
DEBUG: timed out waiting for ping from <Node(0x4d91@46.105.115.90)>
DEBUG: bonding completed successfully with <Node(0x4d91@46.105.115.90)>
DEBUG: poll 26.533 ms took 2.625 ms: 1 events
DEBUG: <<< ping from <Node(0x2b29@75.141.166.249)>
DEBUG: >>> ponging <Node(0x2b29@75.141.166.249)>
DEBUG: timed out waiting for ping from <Node(0xf48a@93.115.29.168)>
DEBUG: bonding completed successfully with <Node(0xf48a@93.115.29.168)>
DEBUG: timed out waiting for ping from <Node(0xd0aa@41.96.160.194)>
DEBUG: bonding completed successfully with <Node(0xd0aa@41.96.160.194)>
DEBUG: timed out waiting for ping from <Node(0x628b@104.211.181.7)>
DEBUG: bonding completed successfully with <Node(0x628b@104.211.181.7)>
DEBUG: timed out waiting for ping from <Node(0xd2e5@118.178.182.73)>
DEBUG: bonding completed successfully with <Node(0xd2e5@118.178.182.73)>
DEBUG: bonded with 8 candidates
DEBUG: node lookup; querying [<Node(0xdb9c@121.40.178.165)>, <Node(0x54f0@149.56.245.193)>, <Node(0x0136@188.32.187.192)>]
DEBUG: >>> find_node to <Node(0x54f0@149.56.245.193)>
DEBUG: >>> find_node to <Node(0x0136@188.32.187.192)>
DEBUG: >>> find_node to <Node(0xdb9c@121.40.178.165)>
DEBUG: poll 888.321 ms took 11.437 ms: 1 events
DEBUG: <<< neighbours from <Node(0x54f0@149.56.245.193)>: [<Node(0x8e74@188.138.1.237)>, <Node(0x195c@46.101.143.7)>, <Node(0x2c2f@66.147.230.39)>, <Node(0xd37e@18.217.146.84)>, <Node(0x6716@209.0.141.27)>, <Node(0x4ae1@93.104.122.48)>, <Node(0xdb59@180.173.197.124)>, <Node(0x647a@84.29.40.212)>, <Node(0xca6a@136.243.66.23)>, <Node(0x88a1@52.58.57.93)>, <Node(0x7ec5@121.225.166.72)>, <Node(0x5c30@176.9.154.84)>]
DEBUG: poll 856.706 ms took 0.014 ms: 1 events
DEBUG: <<< neighbours from <Node(0x54f0@149.56.245.193)>: [<Node(0x7136@213.133.111.201)>, <Node(0x9641@47.95.32.206)>, <Node(0x6357@103.235.247.144)>, <Node(0x423e@178.63.9.8)>]
DEBUG: got expected neighbours response from <Node(0x54f0@149.56.245.193)>
DEBUG: got 9 new candidates
DEBUG: >>> pinging <Node(0x7136@213.133.111.201)>
DEBUG: >>> pinging <Node(0x423e@178.63.9.8)>
DEBUG: >>> pinging <Node(0x7ec5@121.225.166.72)>
DEBUG: >>> pinging <Node(0xdb59@180.173.197.124)>
DEBUG: >>> pinging <Node(0x4ae1@93.104.122.48)>
DEBUG: >>> pinging <Node(0x9641@47.95.32.206)>
DEBUG: >>> pinging <Node(0x6716@209.0.141.27)>
DEBUG: >>> pinging <Node(0xd37e@18.217.146.84)>
DEBUG: >>> pinging <Node(0x88a1@52.58.57.93)>
DEBUG: poll 800.327 ms took 8.873 ms: 1 events
DEBUG: <<< pong from <Node(0x6716@209.0.141.27)>
DEBUG: got expected pong with pingid 0xad6a9e031e3701613e78e583f2f24f74c705fe95fcd0e295b568f09a4b485ed367169fbeded30f23c0c2697d7583ff05e348d44ddb2281e3f902c48db5c6ff0f6ecb543d098d36b531983b3ccad1f1c9ba39924b52c4c8b8e7a46953048814b2
DEBUG: poll 774.395 ms took 8.802 ms: 1 events
DEBUG: <<< pong from <Node(0xd37e@18.217.146.84)>
DEBUG: <<< neighbours from <Node(0x0136@188.32.187.192)>: [<Node(0x81b7@34.207.128.31)>, <Node(0x195c@46.101.143.7)>, <Node(0x2fec@145.239.144.185)>, <Node(0x2df2@96.244.252.244)>, <Node(0x5fca@47.95.32.49)>, <Node(0xf713@1.203.183.99)>, <Node(0xca6a@136.243.66.23)>, <Node(0x88a1@52.58.57.93)>, <Node(0xfafe@86.86.183.108)>, <Node(0xbc40@74.67.65.134)>, <Node(0xa068@59.124.28.244)>, <Node(0x0816@75.175.19.14)>]
DEBUG: <<< neighbours from <Node(0x0136@188.32.187.192)>: [<Node(0x7d79@139.59.190.144)>, <Node(0x6357@103.235.247.144)>, <Node(0x3d2d@162.220.63.233)>, <Node(0xe806@212.8.242.197)>]
DEBUG: got expected pong with pingid 0xff668ff520c42bc265931bf5dbe0b7e245787849cc33bd2e06c3af395b63613ed37ef01c71f4dbdde77a54328db4949e8af9020465ade93a148f3203af87278a894209d6d6bdcedcc3afda22c80649046859edec04213ab324b59e6656c4043b
DEBUG: <<< pong from <Node(0x7136@213.133.111.201)>
DEBUG: unexpected pong from <Node(0x7136@213.133.111.201)> with pingid 0x570339f6113b8772573c0b890e1b251a1f8fb587407d10ac34a4b78abc3830f671361e70da83b284955ae97ee9d855867f2001a3c08b0a821c3aeac5630456490c0baa96ad91ea9f45828b0be8e0f5dad0d8ae54bca6615a3580ccd516fce09a, probably came too late
DEBUG: <<< pong from <Node(0x423e@178.63.9.8)>
DEBUG: got expected neighbours response from <Node(0x0136@188.32.187.192)>
DEBUG: got 8 new candidates
DEBUG: <<< ping from <Node(0x423e@178.63.9.8)>
DEBUG: >>> ponging <Node(0x423e@178.63.9.8)>
DEBUG: >>> pinging <Node(0xf713@1.203.183.99)>
DEBUG: >>> pinging <Node(0x5fca@47.95.32.49)>
DEBUG: >>> pinging <Node(0x81b7@34.207.128.31)>
DEBUG: >>> pinging <Node(0xa068@59.124.28.244)>
DEBUG: >>> pinging <Node(0x3d2d@162.220.63.233)>
DEBUG: >>> pinging <Node(0x0816@75.175.19.14)>
DEBUG: >>> pinging <Node(0x7d79@139.59.190.144)>
DEBUG: >>> pinging <Node(0xbc40@74.67.65.134)>
DEBUG: <<< pong from <Node(0x88a1@52.58.57.93)>
DEBUG: got expected pong with pingid 0x9274bc9bb79a910fd3127ecf0d2e22a3a179a7fbcd5adcffc31bab7c07d9eaac423ea050d5029db1b941aad01714631cc5a76a7e03a6295a71e63bbef71c5b601113c1fa25af3f5679836ae3e18145b3de12ad2b317240dd4d91e18ce29e544b
DEBUG: <<< pong from <Node(0x81b7@34.207.128.31)>
DEBUG: <<< neighbours from <Node(0xdb9c@121.40.178.165)>: [<Node(0x21e6@93.193.95.115)>, <Node(0x5ebb@115.227.226.239)>, <Node(0xc621@47.94.57.152)>, <Node(0x195c@46.101.143.7)>, <Node(0x19dc@121.196.232.205)>, <Node(0xcc35@108.18.247.136)>, <Node(0xadc2@24.22.22.19)>, <Node(0xe9bf@5.12.254.16)>, <Node(0xc9d6@185.56.130.79)>, <Node(0x3879@173.174.110.98)>, <Node(0x5fca@47.95.32.49)>, <Node(0xca6a@136.243.66.23)>]
DEBUG: got expected pong with pingid 0x3507ed0a03d601acae6d5337e8c9bf93aa43216bad03f00b23411f62cd3d096a88a1816445c37d24383f84e3784179ece287279e752c7b3f7d449d7123a71940d38032b357548a43c92c1d3a6f76af1df95d3339ae8a48e86a69da3d0e2fd0ef
DEBUG: <<< neighbours from <Node(0xdb9c@121.40.178.165)>: [<Node(0x161d@46.35.253.127)>, <Node(0x9641@47.95.32.206)>, <Node(0x80ab@103.36.139.135)>, <Node(0xc07c@82.208.100.139)>]
DEBUG: got expected pong with pingid 0xf9d89f7ff0738b8693ccb1acdccddbfea8b45af7a75ee7bc9a9a90bbf6e0d13c81b7bec89fa243549263d987461756ecec1220320ca2f7044172a95b6adf3383324d7774e9993d7cb494cad1547dcf44d63d4043a22b98d01a3820985b282834
DEBUG: <<< pong from <Node(0x9641@47.95.32.206)>
DEBUG: <<< ping from <Node(0x9641@47.95.32.206)>
DEBUG: >>> ponging <Node(0x9641@47.95.32.206)>
DEBUG: got expected neighbours response from <Node(0xdb9c@121.40.178.165)>
DEBUG: got 8 new candidates
DEBUG: <<< pong from <Node(0xbc40@74.67.65.134)>
DEBUG: >>> pinging <Node(0x3879@173.174.110.98)>
DEBUG: >>> pinging <Node(0xc9d6@185.56.130.79)>
DEBUG: >>> pinging <Node(0xe9bf@5.12.254.16)>
DEBUG: >>> pinging <Node(0x161d@46.35.253.127)>
DEBUG: >>> pinging <Node(0x5ebb@115.227.226.239)>
DEBUG: >>> pinging <Node(0xcc35@108.18.247.136)>
DEBUG: >>> pinging <Node(0xadc2@24.22.22.19)>
DEBUG: >>> pinging <Node(0xc07c@82.208.100.139)>
DEBUG: got expected pong with pingid 0x7afe38da2faba46ec8992db713b44f85ca66d168448bdf61daf016b15800c84696415c490f639af511cff71978c8271a7d0ee518f6f24bad8affabc732b1e445373a3f80f51c25cbb15cd41fa04b98a38a98ccb10cd4e381944e68dd8825a15b
DEBUG: <<< pong from <Node(0x7d79@139.59.190.144)>
DEBUG: got expected pong with pingid 0x7c86fe31f68ca6a47122d892865862ce8f610d7fa7591c1f10c1d9d606a57422bc40e510b2ea3e35530816ca6807b917a6d3e9aae076eeda602978efda810ff0134e42d3c3fd57a7956ced01f4187710eca74f7f584ce84355205b8afcf293ea
DEBUG: got expected pong with pingid 0x736e23ab738b253c36fa0885dd0b90bc910acd9fb39535c872bf8e867bf1e0637d793e4fbdedc450358400ee9f59645b6e58a2784de4901e6508934333a6af5e399535f0ff3d1f6413c4f636f0c1dac3fc59ca97837783a09430a4fc4c673766
DEBUG: poll 497.486 ms took 20.137 ms: 1 events
DEBUG: <<< pong from <Node(0x5fca@47.95.32.49)>
DEBUG: <<< ping from <Node(0x5fca@47.95.32.49)>
DEBUG: >>> ponging <Node(0x5fca@47.95.32.49)>
DEBUG: <<< pong from <Node(0x3879@173.174.110.98)>
DEBUG: got expected pong with pingid 0x876da75612337158c29883113151a332fba7b6daefcfda28e5860f031b9e1d375fca7b3b30157784448c09dac25b4e02f9fd0abff060a2b4aa1e752516ffc0de92ddb7af2463f9a9186398dd1c659adf7cf40fe0437bc196b47d48e571c0778c
DEBUG: <<< ping from <Node(0x3879@173.174.110.98)>
DEBUG: >>> ponging <Node(0x3879@173.174.110.98)>
DEBUG: <<< pong from <Node(0xf713@1.203.183.99)>
DEBUG: got expected pong with pingid 0x6d5941e6c9c76ee8857d1ebb204343c29788386c9d6c3512027546c9fe37926f3879fd200f4c0ff84255e2bd2daa4d600b0ab29c432304f13e6251e96ba781b4f275a24f4e3788680f33112949a0f1c1864b9e990d7d90dc4a416e4394e29ff5
DEBUG: got expected pong with pingid 0x26638131c4775420dc2b629066288fc7f08895a5a818e5061e6628e7cd0088f1f71384ef1b7fa1d902ed4cb88f3701727324fd5e0c0a90f5c941d2f65a69e9688de79fca929de15bd9f4be6b9bbe7e34e3662dece3ffc45ee3deed544d5bfd50
DEBUG: poll 394.172 ms took 18.880 ms: 1 events
DEBUG: <<< pong from <Node(0x161d@46.35.253.127)>
DEBUG: got expected pong with pingid 0x6d3a4a27b7a5921e5a34ebb11ff4225372807df758cc419984fd1d88a86e2c39161d73b0508ce025749295d6ab27a766441b4549c427d2e9efe7512245cb3f170a082af3ac831bb6052723e8783d39ad53e9d5228090e96ad1d62e18f0755cfe
DEBUG: poll 358.210 ms took 164.761 ms: 1 events
DEBUG: <<< pong from <Node(0x5ebb@115.227.226.239)>
DEBUG: <<< ping from <Node(0x5ebb@115.227.226.239)>
DEBUG: >>> ponging <Node(0x5ebb@115.227.226.239)>
DEBUG: got expected pong with pingid 0x1dc69b325b4310e8ae069493fdb4602ec768c829511284dd67aaea895ce985175ebbb7c5f1dde57e91f2d8bc81b5e58c583a446556e5b2a7aa0702cc36ec9fdedaf0e9c40fd7300aa4f49ffb87a3a7a981df162b31e2baf462a77a26d187497e
DEBUG: timed out waiting for pong with pingid 0x2d184e3f75c64c99f95c1b1b919c41842c704dd5e0fb09a143ca6fe7fdbca8ac71361e70da83b284955ae97ee9d855867f2001a3c08b0a821c3aeac5630456490c0baa96ad91ea9f45828b0be8e0f5dad0d8ae54bca6615a3580ccd516fce09a
DEBUG: bonding failed, didn't receive pong from <Node(0x7136@213.133.111.201)>
DEBUG: timed out waiting for pong with pingid 0x7c3f37304b8826e1f27475d8b810ef5a6f305ae649dd92f0e8e14e2044e81b8e7ec5e61d504cce17a5c5788e58fd5a995755147dbd191685f1254db59d25c4aabbc0b9c9499b6dc139f617e8978ef3eb20f4f110c64cefceaa1fa9c229627021
DEBUG: bonding failed, didn't receive pong from <Node(0x7ec5@121.225.166.72)>
DEBUG: timed out waiting for pong with pingid 0x0dd0cc6ff5b0b5cd96c4c2b7115d2a8a813da42f130a2dabd764fdc696cc0890db59ca2bb693ea395e0f7e623e085f37465c85b77b7ff4835ab40b9c63b93177080f260b33636b7dae5212fa7d48cda69bf9f2be75e8b6163d17667b3bb8757a
DEBUG: bonding failed, didn't receive pong from <Node(0xdb59@180.173.197.124)>
DEBUG: timed out waiting for pong with pingid 0xcfa4700739654edeac0918e2721a7fdabb9c7cf11cb1d7afab17f94df711bd044ae1ab36b3748fe759969c6cae72862eef3fb4273521082ba09375c33d5b21f8cc7d3f3e1728f509e43df28bdd401db8f450cb32fce1527e60e2be43cf9b360d
DEBUG: bonding failed, didn't receive pong from <Node(0x4ae1@93.104.122.48)>
DEBUG: timed out waiting for ping from <Node(0x6716@209.0.141.27)>
DEBUG: bonding completed successfully with <Node(0x6716@209.0.141.27)>
DEBUG: timed out waiting for ping from <Node(0xd37e@18.217.146.84)>
DEBUG: bonding completed successfully with <Node(0xd37e@18.217.146.84)>
DEBUG: timed out waiting for pong with pingid 0x36126b0520124804806adfb59b4b6e59788d5bd80b9d768f28890d932959973ba068c2633a98f41f3737b52a287ac98cc0bf330d8ffc2cf96894adddb84fe1f422ec718a395fe551860be307062acda05c593c8bdba5b98e16918185b01b294b
DEBUG: bonding failed, didn't receive pong from <Node(0xa068@59.124.28.244)>
DEBUG: timed out waiting for pong with pingid 0x83b33068d7153d83152bce5a1e842fc5d8e469d3d9e80ea1115e003c6efd2a683d2d123871005a6f27cd3aa29729df87e4cb22053f283eae0ee3bb33267bf248e220d9fb978bf8ef2bf142e42a05ff06f70c8f5500dd76c1fe1a135dd7e3518c
DEBUG: bonding failed, didn't receive pong from <Node(0x3d2d@162.220.63.233)>
DEBUG: timed out waiting for pong with pingid 0x766a09b96b8d70766b2000e0b7827db5fb8ee5ed1324f2578c7eb1a12cbc3773081602dc415518e2cbe9ce23735fefff283ae63861002da70e26ff25599bd5efdc94f44019563c74d5556a9c2b6616e5bab04f0a593488cd16fff257aa38fd5d
DEBUG: bonding failed, didn't receive pong from <Node(0x0816@75.175.19.14)>
DEBUG: timed out waiting for ping from <Node(0x423e@178.63.9.8)>
DEBUG: bonding completed successfully with <Node(0x423e@178.63.9.8)>
DEBUG: timed out waiting for ping from <Node(0x88a1@52.58.57.93)>
DEBUG: bonding completed successfully with <Node(0x88a1@52.58.57.93)>
DEBUG: timed out waiting for ping from <Node(0x81b7@34.207.128.31)>
DEBUG: bonding completed successfully with <Node(0x81b7@34.207.128.31)>
DEBUG: timed out waiting for pong with pingid 0x7a6144548cd0564fefadac2e7d4da0f2ade39a1c0ce619f15f69c30d35eedd5fc9d66b404a93b78d8744581d17fc8a3bca9fd1d061d6d0cbcd80869122676e901a5128f77d15d70eb21d80a9e93868a06316405a11ebba04df812a9d5eb8db87
DEBUG: bonding failed, didn't receive pong from <Node(0xc9d6@185.56.130.79)>
DEBUG: timed out waiting for pong with pingid 0x7d9dd18e3d909c1fcc529b9854cba992456c070423ba24937cce08e6de6550e3e9bf2d51b497bf98a3fed31a6b818cdc9a338d40968dd3de9c09ecb8049280874eb64a53baf426401d6121ab8a0df915ea41b09377b60b297066d67e267e7dbf
DEBUG: bonding failed, didn't receive pong from <Node(0xe9bf@5.12.254.16)>
DEBUG: timed out waiting for pong with pingid 0x3dcbae9e29da54b03ddf71ecad52eb9e6b3e39db490571d62df37a98cc1d8424cc358e78acef7fc1b3369721c7dfb32bb17134095528ee4b549cbfd08c8dce911aae46b9f7f6f274ef7c2f4d31d9d934137dc4b0d9bb94863a63a50b91345219
DEBUG: bonding failed, didn't receive pong from <Node(0xcc35@108.18.247.136)>
DEBUG: timed out waiting for pong with pingid 0x6e37ad7991fb96e07125f3e4b020ffb3dd587c952c76b74384d03729fea01fdfadc2f587ea42888754016cf5794e76afc000b168a723e4b31f8714e8c5c9d509388185bd68fc339b7e0e4b55b5af86fe8ebf643d22e474f965e9bdf1064cdf8f
DEBUG: bonding failed, didn't receive pong from <Node(0xadc2@24.22.22.19)>
DEBUG: timed out waiting for pong with pingid 0x0aa349e02035e2e0f99ae4122702827cbc11c331d4e524380fa88b349b80b773c07c6e0cd9f2cf138b6dacdaf25b252bc39915dd277a30e436b7ac3be20f50c8d7c707989e0ddccd4381da2e9d717580f485019fb7663ab1aee320fd53c0591e
DEBUG: bonding failed, didn't receive pong from <Node(0xc07c@82.208.100.139)>
DEBUG: timed out waiting for ping from <Node(0x9641@47.95.32.206)>
DEBUG: bonding completed successfully with <Node(0x9641@47.95.32.206)>
DEBUG: bonded with 5 candidates
DEBUG: timed out waiting for ping from <Node(0xbc40@74.67.65.134)>
DEBUG: bonding completed successfully with <Node(0xbc40@74.67.65.134)>
DEBUG: timed out waiting for ping from <Node(0x7d79@139.59.190.144)>
DEBUG: bonding completed successfully with <Node(0x7d79@139.59.190.144)>
DEBUG: timed out waiting for ping from <Node(0x5fca@47.95.32.49)>
DEBUG: bonding completed successfully with <Node(0x5fca@47.95.32.49)>
DEBUG: timed out waiting for ping from <Node(0x3879@173.174.110.98)>
DEBUG: bonding completed successfully with <Node(0x3879@173.174.110.98)>
DEBUG: timed out waiting for ping from <Node(0xf713@1.203.183.99)>
DEBUG: bonding completed successfully with <Node(0xf713@1.203.183.99)>
DEBUG: bonded with 5 candidates
DEBUG: timed out waiting for ping from <Node(0x161d@46.35.253.127)>
DEBUG: bonding completed successfully with <Node(0x161d@46.35.253.127)>
DEBUG: timed out waiting for ping from <Node(0x5ebb@115.227.226.239)>
DEBUG: bonding completed successfully with <Node(0x5ebb@115.227.226.239)>
DEBUG: bonded with 3 candidates
DEBUG: node lookup; querying [<Node(0x9c65@188.166.223.208)>]
DEBUG: >>> find_node to <Node(0x9c65@188.166.223.208)>
DEBUG: poll 899.600 ms took 401.171 ms: 1 events
DEBUG: <<< neighbours from <Node(0x9c65@188.166.223.208)>: [<Node(0x4544@99.109.160.170)>, <Node(0x195c@46.101.143.7)>, <Node(0x7181@119.28.9.133)>, <Node(0x6fb2@120.76.100.97)>, <Node(0x9039@108.39.204.189)>, <Node(0xb84c@173.49.206.26)>, <Node(0x2fec@145.239.144.185)>, <Node(0xb400@76.21.179.177)>, <Node(0x83c3@165.227.214.75)>, <Node(0x647a@84.29.40.212)>, <Node(0x3879@173.174.110.98)>, <Node(0x37aa@108.28.94.150)>]
DEBUG: poll 477.704 ms took 0.024 ms: 1 events
DEBUG: <<< neighbours from <Node(0x9c65@188.166.223.208)>: [<Node(0xf583@71.86.108.250)>, <Node(0xdf99@87.6.155.233)>, <Node(0xc381@65.31.129.129)>, <Node(0xcf9b@178.238.226.75)>]
DEBUG: got expected neighbours response from <Node(0x9c65@188.166.223.208)>
DEBUG: got 9 new candidates
DEBUG: >>> pinging <Node(0xcf9b@178.238.226.75)>
DEBUG: >>> pinging <Node(0x6fb2@120.76.100.97)>
DEBUG: >>> pinging <Node(0xf583@71.86.108.250)>
DEBUG: >>> pinging <Node(0xb84c@173.49.206.26)>
DEBUG: >>> pinging <Node(0xdf99@87.6.155.233)>
DEBUG: >>> pinging <Node(0xc381@65.31.129.129)>
DEBUG: >>> pinging <Node(0x37aa@108.28.94.150)>
DEBUG: >>> pinging <Node(0x7181@119.28.9.133)>
DEBUG: >>> pinging <Node(0xb400@76.21.179.177)>
DEBUG: <<< pong from <Node(0xb84c@173.49.206.26)>
DEBUG: <<< ping from <Node(0xb84c@173.49.206.26)>
DEBUG: >>> ponging <Node(0xb84c@173.49.206.26)>
DEBUG: got expected pong with pingid 0x2e6fd7ec9b101655be7a9250aa040b3f84d4961b71391cd5c7ac2bb3b9c77ecdb84c54dc0d2c097d05a2e1c7151e05e952297724591bdbeccb9c27f7578fc2ced021b32282236d0001953efc2dfae8ba6160a1fdb6b844cd92300c4a607e7e67
DEBUG: poll 827.840 ms took 2.973 ms: 1 events
DEBUG: <<< pong from <Node(0x37aa@108.28.94.150)>
DEBUG: <<< ping from <Node(0x37aa@108.28.94.150)>
DEBUG: >>> ponging <Node(0x37aa@108.28.94.150)>
DEBUG: got expected pong with pingid 0x819537c312c64a94f9f1cb078d6e603b395849e45eae46cf21ff519848815a8f37aae5f9899b98afb0da5de0365395245853746acb8d551753000c9366a18376b86891032b9edd7670d2cabd9c8bc24ddff2093bd13d2e772bacdf95e894e4c6
DEBUG: poll 791.334 ms took 187.457 ms: 1 events
DEBUG: <<< pong from <Node(0x6fb2@120.76.100.97)>
DEBUG: unexpected pong from <Node(0x6fb2@120.76.100.97)> with pingid 0x9d7205754602ef189336f8fa206041a63747bd98d9b7da6d10e8a30c09dbe5626fb21a118fcea9c139f7f9dbb901a7172f3d2fb3a30c62cfa64a706486af149201f2424e2a27dc2967d7cf39be31e21ddb44efc72c79a250a9aa2cebb0602b3b, probably came too late
DEBUG: poll 587.394 ms took 358.740 ms: 1 events
DEBUG: <<< pong from <Node(0xc381@65.31.129.129)>
DEBUG: <<< ping from <Node(0xc381@65.31.129.129)>
DEBUG: >>> ponging <Node(0xc381@65.31.129.129)>
DEBUG: got expected pong with pingid 0x4b8d397676404634a10fa768f57a29653f62a4d6ff87bbf1f64bd214948a6ef9c3814e36d9a3f24dc88701fb0e6725f48f941dfca141d75b3900bfd347d8ed9c43f460796ec3dfd4bd3ac89b60a2ac633823f83794091b2a387980ae245967a7
DEBUG: timed out waiting for pong with pingid 0xf44f05d2ac96044fe5fed506883634e5aa5f205ef31d86c33a1a597a2fdf83a0cf9b5a0e37953d94a86de973a94ea49582002a3cdbfcc9bed9c0e14182a4ad9972dbdbec824a80c2a49a77f37a4639aeb3ce43a0e5476df63b02d42c3859bec4
DEBUG: bonding failed, didn't receive pong from <Node(0xcf9b@178.238.226.75)>
DEBUG: timed out waiting for pong with pingid 0x1b792ee2521519241fdcc6f77fc34d2ccdf33205c38f189c1e8c45908e0194796fb21a118fcea9c139f7f9dbb901a7172f3d2fb3a30c62cfa64a706486af149201f2424e2a27dc2967d7cf39be31e21ddb44efc72c79a250a9aa2cebb0602b3b
DEBUG: bonding failed, didn't receive pong from <Node(0x6fb2@120.76.100.97)>
DEBUG: timed out waiting for pong with pingid 0x8b51dd4b4b57ae16e018b901d66dde355834588942cd15731d588f02f7ee9b5af5838aad38285ef6996f31ab38564fe2174cbbdd5c598ca815f41ab9b1e711845cedcb931b10bcbe7589827381f6422569813f87f4d7a0948aedc8c86962000d
DEBUG: bonding failed, didn't receive pong from <Node(0xf583@71.86.108.250)>
DEBUG: timed out waiting for pong with pingid 0x0a4fa1dd1284316f6e0c56ece04dc5cc6b679a9d668b0bc26100d24940568e1adf99c7b76b3aba38a4b335cd8d4cfff5bafa296692beb38e99e3f8e6f0cb79dfb0762bbd105f250c4cbcb50df13ddd12430f05af2de6b4c33fb7ef1c1fc91fe1
DEBUG: bonding failed, didn't receive pong from <Node(0xdf99@87.6.155.233)>
DEBUG: timed out waiting for pong with pingid 0x8a87515853216bba8d21b049e8fa85f1cd98cf5c4923d0c061b0e3ae71b0b5e0718190223bac934f7d4d81972848487cedc71abb5ed761b8e52f19d4740139ed6e3593bf20869c86c93d0e4cf9b29c9b399199033aa4a91a8f13f1e0b32b8147
DEBUG: bonding failed, didn't receive pong from <Node(0x7181@119.28.9.133)>
DEBUG: timed out waiting for pong with pingid 0xb6c7ba141aeecfd51691a86ebb006b25b8968b21dec33f08d1b3d823021727d6b400a22b468c46659b1e1a3907ad909e30b8dffa54f140a080ee420fbe177207120c8fa11b1181ba882dc5a6cb48df6f8ada24869ececaeace385e0c21d8abbb
DEBUG: bonding failed, didn't receive pong from <Node(0xb400@76.21.179.177)>
DEBUG: timed out waiting for ping from <Node(0xb84c@173.49.206.26)>
DEBUG: bonding completed successfully with <Node(0xb84c@173.49.206.26)>
DEBUG: timed out waiting for ping from <Node(0x37aa@108.28.94.150)>
DEBUG: bonding completed successfully with <Node(0x37aa@108.28.94.150)>
DEBUG: timed out waiting for ping from <Node(0xc381@65.31.129.129)>
DEBUG: bonding completed successfully with <Node(0xc381@65.31.129.129)>
DEBUG: bonded with 3 candidates
INFO: lookup finished for 74100164683406815212051911074875497894516455655957436483477056869264537760058: [<Node(0x158f@13.75.154.138)>, <Node(0x4a48@139.59.111.210)>, <Node(0x43dd@146.148.112.168)>, <Node(0x1118@52.74.57.123)>, <Node(0x21db@46.43.3.35)>, <Node(0xd8c3@35.189.249.117)>, <Node(0x78de@191.235.84.50)>, <Node(0x1e1b@47.95.225.87)>, <Node(0x48cf@174.65.167.20)>, <Node(0x0dbf@210.55.87.47)>, <Node(0x4b57@13.64.146.159)>, <Node(0x799f@209.239.115.237)>, <Node(0xdb9c@121.40.178.165)>, <Node(0x54f0@149.56.245.193)>, <Node(0x0136@188.32.187.192)>, <Node(0x9c65@188.166.223.208)>]
INFO: stopping discovery
DEBUG: Close <_UnixSelectorEventLoop running=False closed=False debug=True>
