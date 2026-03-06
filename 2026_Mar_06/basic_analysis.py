import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('imdb_top_1000.csv', encoding='latin-1')

# 10년 단위로 칸 나누기, 연도 중 숫자가 아닌건 그냥 삭제해버림
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
df = df.dropna(subset=['Released_Year'])
df['decade'] = ((df['Released_Year'] // 10) * 10).astype(int)

# 장르 쪼개기, 같은 영화여도 여러 장르면 다 분리해놓음
df['genre'] = df['Genre'].str.split(',').apply(lambda x: [i.strip() for i in x])
df_exploded = df.explode('genre')

# 평점 5점 이상 필터링 (top1000 데이터라 쓸모없겠지만 그냥 짜는 코드)
df_filtered = df_exploded[df_exploded['IMDB_Rating'] >= 5.0]

# 장르 그룹화, 과반수 또는 최다 비중 추출
genre_trend = df_filtered.groupby(['decade', 'genre']).size().reset_index(name='count')
top_genre = genre_trend.loc[genre_trend.groupby('decade')['count'].idxmax()]

# 시각화
plt.figure(figsize=(12, 6))
bars = plt.bar(top_genre['decade'].astype(str), top_genre['count'], color='skyblue')

for i, bar in enumerate(bars):
    genre_name = top_genre.iloc[i]['genre']
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             genre_name, ha='center', va='bottom', fontsize=10)


plt.title('movie per decade')
plt.xlabel('decade')
plt.ylabel('number of movies')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# 연도 별로 어떤 장르의 영화가 가장 큰 비중을 차지하는지 막대 그래프로 볼 수 있음