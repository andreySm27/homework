#!/usr/bin/env/ python\
# -*- coding:utf-8 -*-
# vim:fileencoding=utf-8
col=int(input("Count programmer: "));
if col%100>10 and col%100 < 16:
	print(col);print(" програмистов");
elif col%10==1:
	print(col);print(" програмист");
elif col%10>=2 and col%10<5:
	print(col);print(" програмиста");
else:
	print(col);print(" програмистов");
pass;
