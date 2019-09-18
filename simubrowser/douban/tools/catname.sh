#!/usr/bin/env bash
cat ./test.txt | grep -v "导演" | grep -v "编剧" | grep -v "主演" | grep -v "类型" | grep -v "官方网站" | \
    grep -v "制片国家" | grep -v "语言" | grep -v "上映日期" | grep -v "片长" | grep -v "集数" | \
     grep -v "IMDb链接" | grep -v "首播" | grep -v "季数"> test01
