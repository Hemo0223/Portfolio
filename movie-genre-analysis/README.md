# README

언어 순서 <br>
한국어, 영어, 중국어<br>
<br>
Language Order  <br>
Korean, English, Chinese<br>
<br>
语言顺序  <br>
韩语、英语、中文<br
<br>
-----  
<br>
# 프로젝트 개요
<br>
이 프로젝트는 IMDb Top 1000 데이터를 기반으로, 시대별 영화 장르의 변화 추이를 분석하기 위해 제작되었습니다.
연도별 장르 분포를 시각화하여, 특정 시기에 어떤 장르가 두드러졌는지 확인하고 전반적인 트렌드를 파악하는 것을 목표로 합니다.
<br>
## 데이터 소스  
<br>
Kaggle의 IMDb Top 1000 데이터셋을 사용했습니다.
https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
<br>
원본 CSV 파일은 프로젝트 폴더 내에 포함되어 있습니다.
<br>
## 사용 라이브러리  
Pandas  
Matplotlib  
<br>
<br>
# 분석 내용
<br>
1. 기본 트렌드 분석 (basic_analysis.py)  
<br>
연도별로 가장 높은 비중을 차지한 영화 장르를 분석하고, 이를 막대그래프로 시각화했습니다.<br>
이를 통해 시대별 대표 장르의 변화를 한눈에 확인할 수 있습니다.<br>
<br>
2. 세부 비율 분석 (more_analysis.py)  
<br>
상위 3개 장르를 스택형 막대그래프로 시각화하여, 각 장르의 상대적인 비율을 함께 확인할 수 있도록 개선했습니다.<br>
단일 장르뿐 아니라, 주요 장르 간의 비중 변화를 비교할 수 있습니다.<br>
<br>
<br>
## 주요 결과    
<br>
- 시대에 따라 우세한 장르가 변화하는 경향이 확인됨  
- 특정 장르가 지속적으로 상위권을 유지하는 패턴 존재  
- 단일 장르보다 복수 장르의 비율을 함께 볼 때 트렌드 해석이 더 명확해짐  
<br>
<br>
## 향후 개선 방향  
<br>
- 더 많은 데이터셋을 활용한 비교 분석  
- 장르 외 요소(평점, 수익 등)와의 상관관계 분석  
- 시계열 분석 기법을 활용한 트렌드 예측  
<br>
<br>
-----
<br>
<br>
# Project Overview  

This project analyzes trends in movie genres over time using the IMDb Top 1000 dataset.  
It aims to identify how genre popularity has shifted across decades by visualizing the distribution of genres by year.  

## Data Source  

This project uses the IMDb Top 1000 dataset from Kaggle.  
https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows  
  
The raw CSV file is included in the project folder.  
  
## Libraries Used  
Pandas  
Matplotlib  


# Analysis Details  
1. Basic Trend Analysis (basic_analysis.py)  

This script identifies the most dominant genre for each period and visualizes the results using a bar chart.
It provides a clear view of how leading genres have changed over time.

2. Proportion Analysis (more_analysis.py)

This version extends the analysis by visualizing the top three genres as a stacked bar chart.
It shows not only the most dominant genre but also the relative proportions of the top genres, making trends easier to interpret.

## Key Findings
- Genre popularity changes over time
- Some genres consistently remain dominant
- Viewing multiple top genres together provides clearer insight into trends


## Future Improvements

- Expanding analysis with additional datasets
- Exploring correlations with ratings, revenue, etc.
- Applying time-series methods for trend prediction
<br>
<br>
-----
<br>
<br>

# 项目概述

本项目基于 IMDb Top 1000 数据集，对不同时代电影类型的变化趋势进行分析。
通过对各年份的类型分布进行可视化，观察不同年代中主流电影类型的变化情况，并整体把握其发展趋势。

## 数据来源

本项目使用了 Kaggle 上的 IMDb Top 1000 数据集：
https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows

原始 CSV 文件已包含在项目文件夹中。

## 使用库
Pandas
Matplotlib


# 分析内容
1. 基础趋势分析 (basic_analysis.py)

对各个时期占比最高的电影类型进行分析，并通过柱状图进行可视化。
可以直观地观察不同年代主导类型的变化。

2. 比例分析 (more_analysis.py)

在原有基础上扩展，将前三名类型以堆叠柱状图的形式展示。
不仅可以看到最主要的类型，还可以比较不同类型之间的相对比例，使趋势更加清晰。

## 主要结论

- 不同年代的主流电影类型存在明显变化
- 部分类型长期保持较高占比
- 同时观察多个主要类型有助于更准确地理解趋势


## 后续改进方向

- 引入更多数据集进行对比分析
- 探索类型与评分、票房等因素之间的关系
- 使用时间序列方法进行趋势预测
