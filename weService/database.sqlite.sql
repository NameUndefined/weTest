BEGIN TRANSACTION;
INSERT INTO `titles` (id,title) VALUES (1,'党史知识测试20题（测试数据库）');
INSERT INTO `titles` (id,title) VALUES (2,'testDATABASE');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (1,'dx',1,'1，新民主主义革命时期，在上海召开的中国共产党全国代表大会是
','["c"]','["A\uff0e\u4e00\u5927 \u4e8c\u5927 \u4e09\u5927     \n", "B\uff0e\u4e8c\u5927 \u4e09\u5927 \u4e94\u5927  \n", "C\uff0e\u4e00\u5927 \u4e8c\u5927 \u56db\u5927  \n", "D\uff0e\u4e00\u5927 \u56db\u5927 \u4e03\u5927\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (2,'dx',1,'2．中国共产党第______次全国代表大会，制定了作为一个完备形态的政党所不可缺少的民主革命纲领，制定了党的章程，完成了建党任务。
','["b"]','["A\uff0e\u2014    \n", "B\uff0e\u4e8c \n", "C\uff0e\u4e09 \n", "D\uff0e\u56db\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (3,'dx',1,'3．以下没有参加中国共产党第次国代表大会的是______。
','["a"]','["A\uff0e\u9648\u72ec\u79c0   \n", "B\uff0e\u6bdb\u6cfd\u4e1c \n", "C\uff0e\u9a6c\u6797 \n", "D\uff0e\u674e\u8fbe\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (4,'dx',1,'4．中国共产党最早的组织是由______等发起，在______首先建立的。
','["a"]','["A\uff0e\u9648\u72ec\u79c0 \u4e0a\u6d77  \n", "B\uff0e\u674e\u5927\u948a \u5317\u4eac\n", "C\uff0e\u6bdb\u6cfd\u4e1c \u957f\u6c99  \n", "D\uff0e\u8463\u5fc5\u6b66 \u6b66\u6c49\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (5,'dx',1,'5．1941年5月19日，毛泽东在延安部会上作______的报告，第一次明确提出了“实事求是”的思想。
','["a"]','["A\uff0e\u300a\u6539\u9020\u6211\u4eec\u7684\u5b66\u4e60\u300b\n", "B\uff0e\u300a\u8bba\u8054\u5408\u653f\u5e9c\u300b\n", "C\uff0e\u300a\u8bba\u6301\u4e45\u6218\u300b   \n", "D\uff0e\u300a\u65b0\u6c11\u4e3b\u4e3b\u4e49\u8bba\u300b\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (6,'dx',1,'6．以下不属于党的三大作风的内容是______。
','["b"]','["A\uff0e\u7406\u8bba\u548c\u5b9e\u8df5\u76f8\u7ed3\u5408\u7684\u4f5c\u98ce\n", "B\uff0e\u8270\u82e6\u6734\u7d20\u7684\u4f5c\u98ce\n", "C\uff0e\u4e0e\u4eba\u6c11\u7fa4\u4f17\u7d27\u5bc6\u5730\u8054\u7cfb\u5728\u4e00\u8d77\u7684\u4f5c\u98ce\n", "D\uff0e\u6279\u8bc4\u53ca\u81ea\u6211\u6279\u8bc4\u7684\u4f5c\u98ce\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (7,'dx',1,'7．______是共产党区别于其他任何政党的显著标志，是使党的路线、方针得以顺利贯彻的根本保证。
','["b"]','["A\uff0e\u8c03\u67e5\u7814\u7a76 \n", "B\uff0e\u4e09\u5927\u4f5c\u98ce\n", "C\uff0e\u4e24\u4e2a\u52a1\u5fc5 \n", "D\uff0e\u7eaa\u5f8b\u4e25\u660e\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (8,'dx',1,'8．毛泽东在党的______上做报告时提出了“两个务必”的要求：  “务必使同志们继续地保持谦虚、谨慎、不骄、不躁的作风，务必使同志们继续地保持艰苦奋斗的作风。”
','["c"]','["A\uff0e\u4e03\u5927         \n", "B\uff0e\u4e03\u5c4a\u4e09\u4e2d\u5168\u4f1a\n", "C\uff0e\u4e03\u5c4a\u4e8c\u4e2d\u5168\u4f1a \n", "D\uff0e\u516b\u5927\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (9,'dx',1,'9．上海“孤岛”时期是指从______年11月中国军队撤离上海到1941年12月珍珠港事变日军侵入上海租界为止。
','["c"]','["A\uff0e1935  \n", "B\uff0e1936  \n", "C\uff0e1937  \n", "D\uff0e1938\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (10,'dx',1,'10．震惊中外的“五卅”反帝爱国运动爆发的导火线是______被枪杀。
','["a"]','["A\uff0e\u987e\u6b63\u7ea2\n", "B\uff0e\u8305\u4e3d\u745b\n", "C\uff0e\u5f90\u963f\u6885\n", "D\uff0e\u9093\u4e2d\u590f\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (11,'dx',1,'11．上海工人第三次武装起义成功后，成立了上海______政府。
','["d"]','["A\uff0e\u4eba\u6c11 \n", "B\uff0e\u56fd\u6c11\n", "C\uff0e\u9769\u547d  \n", "D\uff0e\u7279\u522b\u5e02\u4e34\u65f6\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (12,'dx',1,'12．田汉、聂耳分别为电影______作词谱曲的主题歌《义勇军进行曲》，成为广大群众久唱不衰的革命歌曲，后成为中华人民共和国国歌。
','["c"]','["A\uff0e\u300a\u6e14\u5149\u66f2\u300b    \n", "B\uff0e\u300a\u5341\u5b57\u8857\u5934\u300b\n", "C\uff0e\u300a\u98ce\u4e91\u513f\u5973\u300b \n", "D\uff0e\u300a\u5927\u8def\u300b\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (13,'dx',1,'13．党的中共十一届三中全会把全党的工作重点转移到______上来，提出了______的重要思想。
','["b"]','["A\uff0e\u793e\u4f1a\u4e3b\u4e49\u73b0\u4ee3\u5316\u5efa\u8bbe  \u6539\u9769\u5f00\u653e\n", "B\uff0e\u7ecf\u6d4e\u5efa\u8bbe  \u6539\u9769\u5f00\u653e\n", "C\uff0e\u6539\u9769\u5f00\u653e  \u5b9e\u4e8b\u6c42\u662f\n", "D\uff0e\u793e\u4f1a\u4e3b\u4e49\u73b0\u4ee3\u5316\u5efa\u8bbe  \u5b9e\u4e8b\u6c42\u662f\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (14,'dx',1,'14．1923年6月12日至20日，中国共产党第三次全国代表大会在广州召开，这次大会的中心议题是______问题。
','["c"]','["A\uff0e\u6b66\u88c5\u6597\u4e89    \n", "B\u3002\u519c\u6c11\u8fd0\u52a8\n", "C\uff0e\u56fd\u5171\u5408\u4f5c   \n", "D\uff0e\u5de5\u4eba\u8fd0\u52a8\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (15,'dx',1,'15．党的七大是中国共产党在民主革命时期召开的极其重要的一次、也是最后一次代表大会。它的一个重大历史性贡献是确立______为党的指导思想并写入党章。
','["b"]','["A\uff0e\u9a6c\u514b\u601d\u5217\u5b81\u4e3b\u4e49  \n", "B\uff0e\u6bdb\u6cfd\u4e1c\u601d\u60f3\n", "C\uff0e\u9093\u5c0f\u5e73\u7406\u8bba    \n", "D\uff0e\u4e09\u4e2a\u4ee3\u8868\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (16,'dx',1,'16．1956年9月15至27日党的八大在北京举行，这次大会明确了国内主要矛盾是______。
','["c"]','["A\uff0e\u65e0\u4ea7\u9636\u7ea7\u548c\u8d44\u4ea7\u9636\u7ea7\u7684\u77db\u76fe\n", "B\uff0e\u4e2d\u534e\u6c11\u65cf\u548c\u5e1d\u56fd\u4e3b\u4e49\u7684\u77db\u76fe\n", "C\uff0e\u843d\u540e\u7684\u7ecf\u6d4e\u6587\u5316\u548c\u4eba\u6c11\u9700\u8981\u4e4b\u95f4\u7684\u77db\u76fe\n", "D\uff0e\u4eba\u6c11\u7fa4\u4f17\u5185\u90e8\u77db\u76fe\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (17,'dx',1,'17．1935年1月，中共中央政治局在长征途中举行______，这次会议是中共历史上生死攸关的转折点。
','["a"]','["A\uff0e\u9075\u4e49\u4f1a\u8bae\n", "B\uff0e\u4fc4\u754c\u4f1a\u8bae\n", "C\uff0e\u6d1b\u5ddd\u4f1a\u8bae\n", "D\uff0e\u53e4\u7530\u4f1a\u8bae\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (18,'dx',1,'18．1935年12月，在瓦窑堡召开的中共中央政治局扩大会议，确立了______的政策。
','["c"]','["A\uff0e\u5168\u56fd\u4eba\u6c11\u603b\u52a8\u5458\n", "B\uff0e\u5168\u56fd\u519b\u4e8b\u603b\u52a8\u5458\n", "C\uff0e\u6297\u65e5\u6c11\u65cf\u7edf\u4e00\u6218\u7ebf\n", "D\uff0e\u56fd\u5171\u5408\u4f5c\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (19,'dx',1,'19．党的十一届六中全会通过的______，标志着党胜利地完成了指导思想上的拨乱反正。
','["b"]','["A\uff0e\u300a\u5173\u4e8e\u82e5\u5e72\u5386\u53f2\u95ee\u9898\u7684\u51b3\u8bae\u300b\n", "B\uff0e\u300a\u5173\u4e8e\u5efa\u56fd\u4ee5\u6765\u515a\u7684\u82e5\u5e72\u5386\u53f2\u95ee\u9898\u7684\u51b3\u8bae\u300b\n", "C\uff0e\u300a\u5173\u4e8e\u515a\u5185\u653f\u6cbb\u751f\u6d3b\u7684\u82e5\u5e72\u51c6\u5219\u300b\n", "D\uff0e\u300a\u5173\u4e8e\u6574\u515a\u7684\u51b3\u5b9a\u300b\n"]');
INSERT INTO `questions` (id,qtype,title_id,questiontext,answer,chooses) VALUES (20,'dx',1,'20．党的______把“三个代表”重要思想和马克思列宁主义、毛泽东思想、邓小平理论一道确立为我们党的指导思想，明确写进党章。
','["c"]','["A\uff0e\u5341\u56db\u5927\n", "B\uff0e\u5341\u4e94\u5927\n", "C\uff0e\u5341\u516d\u5927\n", "D\uff0e\u5341\u4e03\u5927\n"]');
COMMIT;
