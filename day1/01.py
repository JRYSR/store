print("""
日期    服装名称    价格/件    库存数量    销售量/每日
1号	   羽绒服	  253.6	    500	       10
2号	   牛仔裤	  86.3	    600	       60
3号	   风衣	      96.8	    335	       43
4号	   皮草	      135.9	     855	   63
5号	   T血	      65.8	    632	       63
6号	   衬衫	      49.3	    562	      120
7号	   牛仔裤	   86.3	    600	      72
8号	   羽绒服	   253.6	500	      69
9号	   牛仔裤	  86.3	    600	      35
10号	羽绒服	  253.6	    500	     140
11号	牛仔裤	  86.3	    600	      90
12号	皮草	      135.9	     855	  24
13号	T血	      65.8	     632	  45
14号	风衣	      96.8	    335	      25
15号	牛仔裤	  86.3	     600	  60
16号	T血	      65.8	     632	  129
17号	羽绒服	  253.6	     500	  10
18号	风衣	      96.8	      335	  43
19号	T血	      65.8	      632	  63
20号	牛仔裤	  86.3	      600	  60
21号	皮草	      135.9	      855	  63
22号	风衣	      96.8	      335	  60
23号	T血	      65.8	      632	  58
24号	牛仔裤	  86.3	      600	  140
25号	T血	      65.8	      632	  48
26号	风衣	     96.8	      335	  43
27号	皮草	     135.9	      855	  57
28号	羽绒服	 253.6	      500	  10
29号	T血	     65.8	      632	  63
30号	风衣	     96.8	      335	  78
""")
money = 65.8*469+49.3*120+96.8*292+86.3*517+135.9*207+253.6*239
shuliang = 469 + 120 + 292 + 517 + 207 + 239
print("总销售额为：", money)
print("平均每日销售数量：", shuliang // 30)
print("羽绒服销售数量占比：{:.2f}%".format(239 / shuliang * 100))
print("T恤销售数量占比：{:.2f}%".format(469 / shuliang * 100))
print("衬衫销售数量占比：{:.2f}%".format(120 / shuliang * 100))
print("风衣销售数量占比：{:.2f}%".format(292 / shuliang * 100))
print("牛仔裤销售数量占比：{:.2f}%".format(517 / shuliang * 100))
print("皮草销售数量占比：{:.2f}%".format(239 / shuliang * 100))