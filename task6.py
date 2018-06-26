#!/usr/bin/env/ python\
# -*- coding:utf-8 -*-
# vim:fileencoding=utf-8
col=int(input("Count programmer: "));
if col%100>10 and col%100 < 16:
	print(col," програмистов");
elif col%10==1:
	print(col," програмист");
elif col%10>=2 and col%10<5:
	print(col," програмиста");
else:
	print(col," програмистов");
pass;
