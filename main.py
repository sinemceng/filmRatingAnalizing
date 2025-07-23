import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def loadData():
    df=pd.read_csv("C:\\Users\\Sinem\\Desktop\\imdb_list.csv")
    print(df.info())
    return df

def rateOrt(df):
    plt.figure(figsize=(8,6))
    rating_ortalama=df.groupby("year")["rating"].mean()
    plt.bar(rating_ortalama.index,rating_ortalama.values,color="green", width=0.3)
    plt.ylim(0, 9)
    plt.yticks(np.arange(1.0, 9.0, 0.5))
    plt.xticks(ticks=rating_ortalama.index, rotation=45, fontsize=9)
    font1={"family": "serif", "color": "darkred", "size":13}
    font2 = {"family": "serif", "color": "darkblue", "size": 18}
    plt.xlabel("YEAR",fontdict=font1 )
    plt.ylabel("RATING", fontdict=font1)
    plt.title("Average Ratings by Year", fontdict=font2)
    plt.tight_layout()
    plt.grid(True,axis="y",linewidth=0.4,linestyle="--")

    min_year = rating_ortalama.idxmin()       #idxmin(): Bu metod, rating_ortalama içindeki en küçük değere sahip yılı (index) döndürür.
    max_year = rating_ortalama.idxmax()
    plt.text(min_year, rating_ortalama[min_year] + 0.4, 'Min', ha='center', color='red', fontsize=10, fontweight="bold")    #Y ekseninde, barın biraz üstüne yazsın diye 0.2 ekliyoruz
    plt.text(max_year, rating_ortalama[max_year] + 0.4, 'Max', ha='center', color='green', fontsize=10,fontweight="bold")

    for i, v in enumerate(rating_ortalama.values):
        plt.text(rating_ortalama.index[i], v + 0.1, f"{v:.2f}", ha='center', fontsize=9, color='black')

    plt.savefig("rateOrt.png", dpi=300, bbox_inches='tight')
    plt.show()

def bestFilms(df):
    plt.figure(figsize=(10, 7))
    best=df.groupby("year")["rating"].idxmax()
    topRatedFilms=df.loc[best]

    font1 = {"family": "serif", "color": "darkred", "size": 16}
    font2 = {"family": "serif", "color": "darkblue", "size": 18}

    topRatedFilms["film_year"]=topRatedFilms["title"]+"\n("+topRatedFilms["year"].astype(str)+ ")"
    sns.barplot(x="film_year", y="rating",data=topRatedFilms, width=0.3)
    # Başlık ve eksen etiketlerini ayarlama
    plt.title('Highest-Rated Films Per Year (2015-2024)',fontdict=font2)
    plt.xlabel('Film Adı (Yıl)',fontdict=font1)
    plt.ylabel('Reyting',fontdict=font1)

    # X ekseni etiketlerini döndürme (okunabilirlik için)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)

    # Grafiği düzenleme
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()  # Düzenin sıkışmasını engeller

    plt.savefig("bestFilm.png", dpi=300, bbox_inches='tight')
    plt.show()


def genre(df):
    allgenres=df["genre"].str.split(", ").explode()
    #genre de birden fazla tür varsa diye listeye dönüştürüp ordan ayırcaz

    genrecounts=allgenres.value_counts()
    plt.figure(figsize=(12,7))
    sns.barplot(x=genrecounts.index, y=genrecounts.values,color="purple")
    plt.title('Number of Films Released by Genre', fontsize=16,color="darkblue")
    plt.xlabel('Genre', fontsize=14)
    plt.ylabel('Number of Films', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.savefig("genre.png", dpi=300, bbox_inches='tight')
    plt.show()

def ratingDist(df):
    sns.histplot(df["rating"], bins=20, kde=True, color='purple', edgecolor='black')
    plt.title(f"Rating Distribution (n={len(df)})",color="darkblue")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    ortalama = df["rating"].mean()
    plt.axvline(ortalama, color='red', linestyle='dashed', linewidth=1.5, label=f"Average: {ortalama:.2f}")
    plt.legend()

    plt.savefig("ratingDist", dpi=300, bbox_inches='tight')
    plt.show()


def main():
    df=loadData()
    rateOrt(df)
    bestFilms(df)
    genre(df)
    ratingDist(df)
if __name__== "__main__":
    main()