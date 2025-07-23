# Film Verileri Analizi Projesi

Bu proje, film verileri üzerinde derinlemesine bir analiz yaparak sektördeki trendleri, kullanıcı tercihlerini ve film performansını anlamayı amaçlamaktadır. Proje kapsamında veri temizliği, keşifsel veri analizi (EDA) ve görselleştirme teknikleri kullanılarak çeşitli içgörüler elde edilmiştir.

### Veri Yükleme ve Genel Bakış

 `load_data` fonksiyonu kullanılarak veri çerçevesi oluşturulmuştur.
   
 `df.info()` ile veri tipleri ve eksik değerler kontrol edilmiştir.
 
 <img width="506" height="470" alt="Ekran görüntüsü 2025-07-23 142724" src="https://github.com/user-attachments/assets/aa6938b8-664c-451b-95c2-19ae7ae1590e" />


 ### Rating Ortalamaları ve Yıllık Trendler

* `rate_ort(df)` metodu ile her yıl yayınlanan filmlerin ortalama rating'leri hesaplanmıştır.
* Yıllık ortalama rating değişimlerini gösteren bir çizgi grafik oluşturulmuştur.
* En düşük ve en yüksek ortalama rating'e sahip yıllar belirlenmiştir.
  
<img width="2368" height="1769" alt="rateOrt" src="https://github.com/user-attachments/assets/df8a9fef-e289-4e2b-ab5f-408961731084" />


### En Yüksek Rating Alan Filmler

* `bestFilms` analizi ile her yılın en yüksek rating'ine sahip filmleri tespit edilmiştir.
* Bu filmlerin yayın yılları ve rating değerleri arasındaki ilişkiyi gösteren bir görselleştirme yapılmıştır.

<img width="2952" height="2070" alt="bestFilm" src="https://github.com/user-attachments/assets/cf8f01e6-5807-4c78-9ac0-aa0c7da7af9d" />


### Film Türlerinin Dağılımı

* `genre` analizi ile film türlerinin dağılımı incelenmiştir.
* Türlerin popülaritesini gösteren bir `seaborn barplot` kullanılmıştır.

<img width="3570" height="2073" alt="genre" src="https://github.com/user-attachments/assets/99c8af9c-50e1-44a0-b3f9-f680ac7eb531" />


### Rating Dağılımı

* `ratingdist` bölümünde, filmlerin rating dağılımını anlamak için `seaborn.displot` kullanılmıştır.
* Genel izleyici beğenisi hakkında içgörüler elde edilmiştir.

<img width="1688" height="1361" alt="ratingDist" src="https://github.com/user-attachments/assets/7ea79679-a07a-4229-b881-4a1fea9cdf17" />


  ### 📂 Veri Kümesi Bilgisi

- **Kaynak:** [Kaggle - Popular Movies IMDb Reviews Dataset](https://www.kaggle.com/datasets/shivvm/popular-movies-imdb-reviews-dataset)
- **Lisans:** CC0: Public Domain  
- **Açıklama:** Bu projede kullanılan veri seti, IMDb'deki popüler filmlerin yorumlarını ve rating bilgilerini içermektedir. Kaggle kullanıcısı **shivvm** tarafından paylaşılmıştır ve halka açık kullanım için uygundur.
