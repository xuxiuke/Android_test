#coding=utf-8

"""
作者: Duke
文件名: test_step.py
创建时间: 2020/04/08-08:58
"""

from Search_baidu import step
from Search_baidu.open_baidu import Open_baidu
import unittest
import time


# @unittest.skip(u'添加场景、区域，跳过测试')
class Test001(unittest.TestCase, step.Login):  # TestCase类，所有测试用例类继承的基本类
    """登陆测试"""

    # setUp()方法用于测试用例执行前的初始化工作，如打开APP
    def setUp(self):
        self.ina = Open_baidu(self)
        self.ina.open()
        self.driver = self.ina.get_driver()
        self.verificationErrors = []  # 错误信息打印到这个列表
        self.accept_next_alert = True  # 是否继续接受下个警告

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 001
    def test_search_001(self):
        self.assertTrue(self.search())

    # 002
    def test_search_002(self):
        self.assertTrue(self.search())

    # 003
    def test_search_003(self):
        self.assertTrue(self.search())

    # 004
    def test_search_004(self):
        self.assertTrue(self.search())

    # 005
    def test_search_005(self):
        self.assertTrue(self.search())

    # 006
    def test_search_006(self):
        self.assertTrue(self.search())

    # 007
    def test_search_007(self):
        self.assertTrue(self.search())

    # 008
    def test_search_008(self):
        self.assertTrue(self.search())

    # 009
    def test_search_009(self):
        self.assertTrue(self.search())

    # 010
    def test_search_010(self):
        self.assertTrue(self.search())

    # 011
    def test_search_011(self):
        self.assertTrue(self.search())

    # 012
    def test_search_012(self):
        self.assertTrue(self.search())

    # 013
    def test_search_013(self):
        self.assertTrue(self.search())

    # 014
    def test_search_014(self):
        self.assertTrue(self.search())

    # 015
    def test_search_015(self):
        self.assertTrue(self.search())

    # 016
    def test_search_016(self):
        self.assertTrue(self.search())

    # 017
    def test_search_017(self):
        self.assertTrue(self.search())

    # 018
    def test_search_018(self):
        self.assertTrue(self.search())

    # 019
    def test_search_019(self):
        self.assertTrue(self.search())

    # 020
    def test_search_020(self):
        self.assertTrue(self.search())

    # 021
    def test_search_021(self):
        self.assertTrue(self.search())

    # 022
    def test_search_022(self):
        self.assertTrue(self.search())

    # 023
    def test_search_023(self):
        self.assertTrue(self.search())

    # 024
    def test_search_024(self):
        self.assertTrue(self.search())

    # 025
    def test_search_025(self):
        self.assertTrue(self.search())

    # 026
    def test_search_026(self):
        self.assertTrue(self.search())

    # 027
    def test_search_027(self):
        self.assertTrue(self.search())

    # 028
    def test_search_028(self):
        self.assertTrue(self.search())

    # 029
    def test_search_029(self):
        self.assertTrue(self.search())

    # 030
    def test_search_030(self):
        self.assertTrue(self.search())

    # 031
    def test_search_031(self):
        self.assertTrue(self.search())

    # 032
    def test_search_032(self):
        self.assertTrue(self.search())

    # 033
    def test_search_033(self):
        self.assertTrue(self.search())

    # 034
    def test_search_034(self):
        self.assertTrue(self.search())

    # 035
    def test_search_035(self):
        self.assertTrue(self.search())

    # 036
    def test_search_036(self):
        self.assertTrue(self.search())

    # 037
    def test_search_037(self):
        self.assertTrue(self.search())

    # 038
    def test_search_038(self):
        self.assertTrue(self.search())

    # 039
    def test_search_039(self):
        self.assertTrue(self.search())

    # 040
    def test_search_040(self):
        self.assertTrue(self.search())

    # 041
    def test_search_041(self):
        self.assertTrue(self.search())

    # 042
    def test_search_042(self):
        self.assertTrue(self.search())

    # 043
    def test_search_043(self):
        self.assertTrue(self.search())

    # 044
    def test_search_044(self):
        self.assertTrue(self.search())

    # 045
    def test_search_045(self):
        self.assertTrue(self.search())

    # 046
    def test_search_046(self):
        self.assertTrue(self.search())

    # 047
    def test_search_047(self):
        self.assertTrue(self.search())

    # 048
    def test_search_048(self):
        self.assertTrue(self.search())

    # 049
    def test_search_049(self):
        self.assertTrue(self.search())

    # 050
    def test_search_050(self):
        self.assertTrue(self.search())

    # 051
    def test_search_051(self):
        self.assertTrue(self.search())

    # 052
    def test_search_052(self):
        self.assertTrue(self.search())

    # 053
    def test_search_053(self):
        self.assertTrue(self.search())

    # 054
    def test_search_054(self):
        self.assertTrue(self.search())

    # 055
    def test_search_055(self):
        self.assertTrue(self.search())

    # 056
    def test_search_056(self):
        self.assertTrue(self.search())

    # 057
    def test_search_057(self):
        self.assertTrue(self.search())

    # 058
    def test_search_058(self):
        self.assertTrue(self.search())

    # 059
    def test_search_059(self):
        self.assertTrue(self.search())

    # 060
    def test_search_060(self):
        self.assertTrue(self.search())

    # 061
    def test_search_061(self):
        self.assertTrue(self.search())

    # 062
    def test_search_062(self):
        self.assertTrue(self.search())

    # 063
    def test_search_063(self):
        self.assertTrue(self.search())

    # 064
    def test_search_064(self):
        self.assertTrue(self.search())

    # 065
    def test_search_065(self):
        self.assertTrue(self.search())

    # 066
    def test_search_066(self):
        self.assertTrue(self.search())

    # 067
    def test_search_067(self):
        self.assertTrue(self.search())

    # 068
    def test_search_068(self):
        self.assertTrue(self.search())

    # 069
    def test_search_069(self):
        self.assertTrue(self.search())

    # 070
    def test_search_070(self):
        self.assertTrue(self.search())

    # 071
    def test_search_071(self):
        self.assertTrue(self.search())

    # 072
    def test_search_072(self):
        self.assertTrue(self.search())

    # 073
    def test_search_073(self):
        self.assertTrue(self.search())

    # 074
    def test_search_074(self):
        self.assertTrue(self.search())

    # 075
    def test_search_075(self):
        self.assertTrue(self.search())

    # 076
    def test_search_076(self):
        self.assertTrue(self.search())

    # 077
    def test_search_077(self):
        self.assertTrue(self.search())

    # 078
    def test_search_078(self):
        self.assertTrue(self.search())

    # 079
    def test_search_079(self):
        self.assertTrue(self.search())

    # 080
    def test_search_080(self):
        self.assertTrue(self.search())

    # 081
    def test_search_081(self):
        self.assertTrue(self.search())

    # 082
    def test_search_082(self):
        self.assertTrue(self.search())

    # 083
    def test_search_083(self):
        self.assertTrue(self.search())

    # 084
    def test_search_084(self):
        self.assertTrue(self.search())

    # 085
    def test_search_085(self):
        self.assertTrue(self.search())

    # 086
    def test_search_086(self):
        self.assertTrue(self.search())

    # 087
    def test_search_087(self):
        self.assertTrue(self.search())

    # 088
    def test_search_088(self):
        self.assertTrue(self.search())

    # 089
    def test_search_089(self):
        self.assertTrue(self.search())

    # 090
    def test_search_090(self):
        self.assertTrue(self.search())

    # 091
    def test_search_091(self):
        self.assertTrue(self.search())

    # 092
    def test_search_092(self):
        self.assertTrue(self.search())

    # 093
    def test_search_093(self):
        self.assertTrue(self.search())

    # 094
    def test_search_094(self):
        self.assertTrue(self.search())

    # 095
    def test_search_095(self):
        self.assertTrue(self.search())

    # 096
    def test_search_096(self):
        self.assertTrue(self.search())

    # 097
    def test_search_097(self):
        self.assertTrue(self.search())

    # 098
    def test_search_098(self):
        self.assertTrue(self.search())

    # 099
    def test_search_099(self):
        self.assertTrue(self.search())

    # 100
    def test_search_100(self):
        self.assertTrue(self.search())

    # 101
    def test_search_101(self):
        self.assertTrue(self.search())

    # 102
    def test_search_102(self):
        self.assertTrue(self.search())

    # 103
    def test_search_103(self):
        self.assertTrue(self.search())

    # 104
    def test_search_104(self):
        self.assertTrue(self.search())

    # 105
    def test_search_105(self):
        self.assertTrue(self.search())

    # 106
    def test_search_106(self):
        self.assertTrue(self.search())

    # 107
    def test_search_107(self):
        self.assertTrue(self.search())

    # 108
    def test_search_108(self):
        self.assertTrue(self.search())

    # 109
    def test_search_109(self):
        self.assertTrue(self.search())

    # 110
    def test_search_110(self):
        self.assertTrue(self.search())

    # 111
    def test_search_111(self):
        self.assertTrue(self.search())

    # 112
    def test_search_112(self):
        self.assertTrue(self.search())

    # 113
    def test_search_113(self):
        self.assertTrue(self.search())

    # 114
    def test_search_114(self):
        self.assertTrue(self.search())

    # 115
    def test_search_115(self):
        self.assertTrue(self.search())

    # 116
    def test_search_116(self):
        self.assertTrue(self.search())

    # 117
    def test_search_117(self):
        self.assertTrue(self.search())

    # 118
    def test_search_118(self):
        self.assertTrue(self.search())

    # 119
    def test_search_119(self):
        self.assertTrue(self.search())

    # 120
    def test_search_120(self):
        self.assertTrue(self.search())

    # 121
    def test_search_121(self):
        self.assertTrue(self.search())

    # 122
    def test_search_122(self):
        self.assertTrue(self.search())

    # 123
    def test_search_123(self):
        self.assertTrue(self.search())

    # 124
    def test_search_124(self):
        self.assertTrue(self.search())

    # 125
    def test_search_125(self):
        self.assertTrue(self.search())

    # 126
    def test_search_126(self):
        self.assertTrue(self.search())

    # 127
    def test_search_127(self):
        self.assertTrue(self.search())

    # 128
    def test_search_128(self):
        self.assertTrue(self.search())

    # 129
    def test_search_129(self):
        self.assertTrue(self.search())

    # 130
    def test_search_130(self):
        self.assertTrue(self.search())

    # 131
    def test_search_131(self):
        self.assertTrue(self.search())

    # 132
    def test_search_132(self):
        self.assertTrue(self.search())

    # 133
    def test_search_133(self):
        self.assertTrue(self.search())

    # 134
    def test_search_134(self):
        self.assertTrue(self.search())

    # 135
    def test_search_135(self):
        self.assertTrue(self.search())

    # 136
    def test_search_136(self):
        self.assertTrue(self.search())

    # 137
    def test_search_137(self):
        self.assertTrue(self.search())

    # 138
    def test_search_138(self):
        self.assertTrue(self.search())

    # 139
    def test_search_139(self):
        self.assertTrue(self.search())

    # 140
    def test_search_140(self):
        self.assertTrue(self.search())

    # 141
    def test_search_141(self):
        self.assertTrue(self.search())

    # 142
    def test_search_142(self):
        self.assertTrue(self.search())

    # 143
    def test_search_143(self):
        self.assertTrue(self.search())

    # 144
    def test_search_144(self):
        self.assertTrue(self.search())

    # 145
    def test_search_145(self):
        self.assertTrue(self.search())

    # 146
    def test_search_146(self):
        self.assertTrue(self.search())

    # 147
    def test_search_147(self):
        self.assertTrue(self.search())

    # 148
    def test_search_148(self):
        self.assertTrue(self.search())

    # 149
    def test_search_149(self):
        self.assertTrue(self.search())

    # 150
    def test_search_150(self):
        self.assertTrue(self.search())

    # 151
    def test_search_151(self):
        self.assertTrue(self.search())

    # 152
    def test_search_152(self):
        self.assertTrue(self.search())

    # 153
    def test_search_153(self):
        self.assertTrue(self.search())

    # 154
    def test_search_154(self):
        self.assertTrue(self.search())

    # 155
    def test_search_155(self):
        self.assertTrue(self.search())

    # 156
    def test_search_156(self):
        self.assertTrue(self.search())

    # 157
    def test_search_157(self):
        self.assertTrue(self.search())

    # 158
    def test_search_158(self):
        self.assertTrue(self.search())

    # 159
    def test_search_159(self):
        self.assertTrue(self.search())

    # 160
    def test_search_160(self):
        self.assertTrue(self.search())

    # 161
    def test_search_161(self):
        self.assertTrue(self.search())

    # 162
    def test_search_162(self):
        self.assertTrue(self.search())

    # 163
    def test_search_163(self):
        self.assertTrue(self.search())

    # 164
    def test_search_164(self):
        self.assertTrue(self.search())

    # 165
    def test_search_165(self):
        self.assertTrue(self.search())

    # 166
    def test_search_166(self):
        self.assertTrue(self.search())

    # 167
    def test_search_167(self):
        self.assertTrue(self.search())

    # 168
    def test_search_168(self):
        self.assertTrue(self.search())

    # 169
    def test_search_169(self):
        self.assertTrue(self.search())

    # 170
    def test_search_170(self):
        self.assertTrue(self.search())

    # 171
    def test_search_171(self):
        self.assertTrue(self.search())

    # 172
    def test_search_172(self):
        self.assertTrue(self.search())

    # 173
    def test_search_173(self):
        self.assertTrue(self.search())

    # 174
    def test_search_174(self):
        self.assertTrue(self.search())

    # 175
    def test_search_175(self):
        self.assertTrue(self.search())

    # 176
    def test_search_176(self):
        self.assertTrue(self.search())

    # 177
    def test_search_177(self):
        self.assertTrue(self.search())

    # 178
    def test_search_178(self):
        self.assertTrue(self.search())

    # 179
    def test_search_179(self):
        self.assertTrue(self.search())

    # 180
    def test_search_180(self):
        self.assertTrue(self.search())

    # 181
    def test_search_181(self):
        self.assertTrue(self.search())

    # 182
    def test_search_182(self):
        self.assertTrue(self.search())

    # 183
    def test_search_183(self):
        self.assertTrue(self.search())

    # 184
    def test_search_184(self):
        self.assertTrue(self.search())

    # 185
    def test_search_185(self):
        self.assertTrue(self.search())

    # 186
    def test_search_186(self):
        self.assertTrue(self.search())

    # 187
    def test_search_187(self):
        self.assertTrue(self.search())

    # 188
    def test_search_188(self):
        self.assertTrue(self.search())

    # 189
    def test_search_189(self):
        self.assertTrue(self.search())

    # 190
    def test_search_190(self):
        self.assertTrue(self.search())

    # 191
    def test_search_191(self):
        self.assertTrue(self.search())

    # 192
    def test_search_192(self):
        self.assertTrue(self.search())

    # 193
    def test_search_193(self):
        self.assertTrue(self.search())

    # 194
    def test_search_194(self):
        self.assertTrue(self.search())

    # 195
    def test_search_195(self):
        self.assertTrue(self.search())

    # 196
    def test_search_196(self):
        self.assertTrue(self.search())

    # 197
    def test_search_197(self):
        self.assertTrue(self.search())

    # 198
    def test_search_198(self):
        self.assertTrue(self.search())

    # 199
    def test_search_199(self):
        self.assertTrue(self.search())

    # 200
    def test_search_200(self):
        self.assertTrue(self.search())

    # 201
    def test_search_201(self):
        self.assertTrue(self.search())

    # 202
    def test_search_202(self):
        self.assertTrue(self.search())

    # 203
    def test_search_203(self):
        self.assertTrue(self.search())

    # 204
    def test_search_204(self):
        self.assertTrue(self.search())

    # 205
    def test_search_205(self):
        self.assertTrue(self.search())

    # 206
    def test_search_206(self):
        self.assertTrue(self.search())

    # 207
    def test_search_207(self):
        self.assertTrue(self.search())

    # 208
    def test_search_208(self):
        self.assertTrue(self.search())

    # 209
    def test_search_209(self):
        self.assertTrue(self.search())

    # 210
    def test_search_210(self):
        self.assertTrue(self.search())

    # 211
    def test_search_211(self):
        self.assertTrue(self.search())

    # 212
    def test_search_212(self):
        self.assertTrue(self.search())

    # 213
    def test_search_213(self):
        self.assertTrue(self.search())

    # 214
    def test_search_214(self):
        self.assertTrue(self.search())

    # 215
    def test_search_215(self):
        self.assertTrue(self.search())

    # 216
    def test_search_216(self):
        self.assertTrue(self.search())

    # 217
    def test_search_217(self):
        self.assertTrue(self.search())

    # 218
    def test_search_218(self):
        self.assertTrue(self.search())

    # 219
    def test_search_219(self):
        self.assertTrue(self.search())

    # 220
    def test_search_220(self):
        self.assertTrue(self.search())

    # 221
    def test_search_221(self):
        self.assertTrue(self.search())

    # 222
    def test_search_222(self):
        self.assertTrue(self.search())

    # 223
    def test_search_223(self):
        self.assertTrue(self.search())

    # 224
    def test_search_224(self):
        self.assertTrue(self.search())

    # 225
    def test_search_225(self):
        self.assertTrue(self.search())

    # 226
    def test_search_226(self):
        self.assertTrue(self.search())

    # 227
    def test_search_227(self):
        self.assertTrue(self.search())

    # 228
    def test_search_228(self):
        self.assertTrue(self.search())

    # 229
    def test_search_229(self):
        self.assertTrue(self.search())

    # 230
    def test_search_230(self):
        self.assertTrue(self.search())

    # 231
    def test_search_231(self):
        self.assertTrue(self.search())

    # 232
    def test_search_232(self):
        self.assertTrue(self.search())

    # 233
    def test_search_233(self):
        self.assertTrue(self.search())

    # 234
    def test_search_234(self):
        self.assertTrue(self.search())

    # 235
    def test_search_235(self):
        self.assertTrue(self.search())

    # 236
    def test_search_236(self):
        self.assertTrue(self.search())

    # 237
    def test_search_237(self):
        self.assertTrue(self.search())

    # 238
    def test_search_238(self):
        self.assertTrue(self.search())

    # 239
    def test_search_239(self):
        self.assertTrue(self.search())

    # 240
    def test_search_240(self):
        self.assertTrue(self.search())

    # 241
    def test_search_241(self):
        self.assertTrue(self.search())

    # 242
    def test_search_242(self):
        self.assertTrue(self.search())

    # 243
    def test_search_243(self):
        self.assertTrue(self.search())

    # 244
    def test_search_244(self):
        self.assertTrue(self.search())

    # 245
    def test_search_245(self):
        self.assertTrue(self.search())

    # 246
    def test_search_246(self):
        self.assertTrue(self.search())

    # 247
    def test_search_247(self):
        self.assertTrue(self.search())

    # 248
    def test_search_248(self):
        self.assertTrue(self.search())

    # 249
    def test_search_249(self):
        self.assertTrue(self.search())

    # 250
    def test_search_250(self):
        self.assertTrue(self.search())

    # 251
    def test_search_251(self):
        self.assertTrue(self.search())

    # 252
    def test_search_252(self):
        self.assertTrue(self.search())

    # 253
    def test_search_253(self):
        self.assertTrue(self.search())

    # 254
    def test_search_254(self):
        self.assertTrue(self.search())

    # 255
    def test_search_255(self):
        self.assertTrue(self.search())

    # 256
    def test_search_256(self):
        self.assertTrue(self.search())

    # 257
    def test_search_257(self):
        self.assertTrue(self.search())

    # 258
    def test_search_258(self):
        self.assertTrue(self.search())

    # 259
    def test_search_259(self):
        self.assertTrue(self.search())

    # 260
    def test_search_260(self):
        self.assertTrue(self.search())

    # 261
    def test_search_261(self):
        self.assertTrue(self.search())

    # 262
    def test_search_262(self):
        self.assertTrue(self.search())

    # 263
    def test_search_263(self):
        self.assertTrue(self.search())

    # 264
    def test_search_264(self):
        self.assertTrue(self.search())

    # 265
    def test_search_265(self):
        self.assertTrue(self.search())

    # 266
    def test_search_266(self):
        self.assertTrue(self.search())

    # 267
    def test_search_267(self):
        self.assertTrue(self.search())

    # 268
    def test_search_268(self):
        self.assertTrue(self.search())

    # 269
    def test_search_269(self):
        self.assertTrue(self.search())

    # 270
    def test_search_270(self):
        self.assertTrue(self.search())

    # 271
    def test_search_271(self):
        self.assertTrue(self.search())

    # 272
    def test_search_272(self):
        self.assertTrue(self.search())

    # 273
    def test_search_273(self):
        self.assertTrue(self.search())

    # 274
    def test_search_274(self):
        self.assertTrue(self.search())

    # 275
    def test_search_275(self):
        self.assertTrue(self.search())

    # 276
    def test_search_276(self):
        self.assertTrue(self.search())

    # 277
    def test_search_277(self):
        self.assertTrue(self.search())

    # 278
    def test_search_278(self):
        self.assertTrue(self.search())

    # 279
    def test_search_279(self):
        self.assertTrue(self.search())

    # 280
    def test_search_280(self):
        self.assertTrue(self.search())

    # 281
    def test_search_281(self):
        self.assertTrue(self.search())

    # 282
    def test_search_282(self):
        self.assertTrue(self.search())

    # 283
    def test_search_283(self):
        self.assertTrue(self.search())

    # 284
    def test_search_284(self):
        self.assertTrue(self.search())

    # 285
    def test_search_285(self):
        self.assertTrue(self.search())

    # 286
    def test_search_286(self):
        self.assertTrue(self.search())

    # 287
    def test_search_287(self):
        self.assertTrue(self.search())

    # 288
    def test_search_288(self):
        self.assertTrue(self.search())

    # 289
    def test_search_289(self):
        self.assertTrue(self.search())

    # 290
    def test_search_290(self):
        self.assertTrue(self.search())

    # 291
    def test_search_291(self):
        self.assertTrue(self.search())

    # 292
    def test_search_292(self):
        self.assertTrue(self.search())

    # 293
    def test_search_293(self):
        self.assertTrue(self.search())

    # 294
    def test_search_294(self):
        self.assertTrue(self.search())

    # 295
    def test_search_295(self):
        self.assertTrue(self.search())

    # 296
    def test_search_296(self):
        self.assertTrue(self.search())

    # 297
    def test_search_297(self):
        self.assertTrue(self.search())

    # 298
    def test_search_298(self):
        self.assertTrue(self.search())

    # 299
    def test_search_299(self):
        self.assertTrue(self.search())

    # 300
    def test_search_300(self):
        self.assertTrue(self.search())