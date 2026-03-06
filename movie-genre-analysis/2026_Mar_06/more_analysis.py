# 260306_1.py 파일에서는 최다비중을 차지하는 장르만 표시했는데, 여기(260326_2.py)에서는 top3장르도 다 표시할 것

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

# 시대별 상위 3개 장르 추출, 나머지는 other로 퉁침
def get_top3_and_others(group):
    top3 = group.nlargest(3, 'count')
    others_count = group['count'].sum() - top3['count'].sum()

    others = pd.DataFrame({
        'decade': [group['decade'].iloc[0]],
        'genre': ['others'],
        'count': [others_count]
    })
    return pd.concat([top3, others])

top3_trend = genre_trend.groupby('decade', group_keys=False).apply(get_top3_and_others)

pivot_df = top3_trend.pivot(index='decade', columns='genre', values='count').fillna(0)

# 시각화
ax = pivot_df.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='tab20', width=0.8)

# 막대 안에 영화 몇 편인가 숫자로 표시
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    if height > 3:
        x, y = p.get_xy() 
        ax.annotate(f'{int(height)}', (x + width/2, y + height/2), 
                    ha='center', va='center', fontsize=9, color='black')

# 영화 장르는 우상단에 써놓음
plt.title('top 3 genres per decade')
plt.xlabel('decade')
plt.ylabel('number of movies')
plt.legend(title='genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 연도 별로 어떤 장르의 영화가 가장 큰 비중을 차지하는지 막대 그래프로 볼 수 있음
# 이로써 2010년대는 드라마, 어드벤처, 액션 순으로 top1000에 포함된 영화가 많았음을 볼 수 있음