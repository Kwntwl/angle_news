B
    �l]�  �            	   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZdZed�Z	e	ek�r�e�
d� dZee�� �Ze j �e�Zee�Zej�e�Ze�dd�Zedd	�Ze�e�Zejd
ed  ddd�d�Ze�� Zeed d  d �Zdeed f Zded  Z deed f Z!ddddddde"e� d�Z#ddddddde"e � d�Z$ddddddde"e!� d�Z%ejded  d�Z&e&j'Z(ejd ed  d�Z)e)j'Z*e�+d!e*�Z,e�+d!e(�Z-e,�.e-� d"d#� Z/ejd$ed  d�Z0e0j'Z1e�+d!e1�Z2d%d&� Z3y�e4e� e&j5d'k�r�e4d(ed d  d)  � e4d*ed d  d+  � e4d,ed d  d- � e4d.ed d/� � e/ee e#e$e,e� e3e!e e#e%e2e� ne4d0� W nD e6k
�r�   e4d1� e�7d2� Y n e8k
�r�   e4d3� Y nX ne4d4� dS )5�    NZbangkez[1;30mPassword: �clearaV  [32m

	 .--.             .-.          .-..-.   
	: .; :            : :          : `: :   
	:    :,-.,-. .--. : :   .--.   : .` :   
	: :: :: ,. :' .; :: :_ ' '_.'  : :. : _ 
	:_;:_;:_;:_;`._. ;`.__;`.__.'  :_;:_;:_;
	             .-. :                      
	             `._.'                      
	[31m[[37mAuthor: Akbar Neotech[31m]
	z%20�+zcfg.json�rz:http://triadnews.xyz/adminpanel/api/get_user_profile?id=%s�user_idzapplication/json�deflate)�AcceptzAccept-Encoding)�url�headers�ALL_IN_ONE_VIDEO�walletz/date=%s&money=0.01&user_id=%s&type=Video+Bonus&zwallet=0.01&user_id=%s&z.date=%s&money=0.01&user_id=%s&type=News+Bonus&z0application/x-www-form-urlencoded; charset=UTF-8z>Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo 1814 Build/O11019)ztriadnews.xyzz
Keep-Alivez%s)zContent-Typez
User-Agent�Host�
ConnectionzAccept-Encodingr   zContent-LengthZgzip)zContent-Typez
User-Agentr   r   r   zAccept-EncodingzContent-LengthzEhttp://triadnews.xyz/adminpanel/api/get_all_videos?&api_key=%s&page=1�api_key)r   z@http://triadnews.xyz/adminpanel/api/get_recent_videos?api_key=%sz"id":(.*?),c             C   s�   t d� x�|D ]�}tjd|d |f d� tjd| |d� tjd||d�}|�� }tjd|d	  d
dd�d�}	|	�� }
t|
d d d �}t d|d d d  d|dd�   � t�d� qW d S )Nu�   
	[34m↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
	[34m| [33mMisi menonton video. [34m|
	[34m↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
zKhttp://triadnews.xyz/adminpanel/api/video_view_count?api_key=%s&video_id=%sr   )r   z=http://triadnews.xyz/adminpanel/api/post_user_transaction_add)r   �datar	   z;http://triadnews.xyz/adminpanel/api/post_user_wallet_updatez:http://triadnews.xyz/adminpanel/api/get_user_profile?id=%sr   zapplication/jsonr   )r   zAccept-Encoding)r   r	   r
   r   r   z[32mBalance has been �msgz [37m| [31m%s�   �
   )�print�requests�get�post�json�str�time�sleep)r   �datas�head�heads�rer�cfg�iZdsZdjZtyZjsorZwal� r!   �bot.py�videoA   s    
(r#   z;http://triadnews.xyz/adminpanel/api/get_cat_list?api_key=%sc             C   s�   t d� x�|D ]�}tjd|d |f d� tjd| |d� tjd||d�}|�� }tjd|d	  d
dd�d�}	|	�� }
t|
d d d �}t d|d d d  d|dd�   � t�d� qW d S )Nu�   
	[34m↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
	[34m| [33mMisi membaca artikel. [34m|
	[34m↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
zMhttp://triadnews.xyz/adminpanel/api/get_cat_news?&api_key=%s&cat_id=%s&page=1r   )r   z=http://triadnews.xyz/adminpanel/api/post_user_transaction_add)r   r   r	   z;http://triadnews.xyz/adminpanel/api/post_user_wallet_updatez:http://triadnews.xyz/adminpanel/api/get_user_profile?id=%sr   zapplication/jsonr   )r   zAccept-Encoding)r   r	   r
   r   r   z[32mBalance has been r   z [37m| [31m%sr   r   )r   r   r   r   r   r   r   r   )�cdatar   r   �chead�reclisr   �xZbukaZcjs�frr   Zwalrr!   r!   r"   �artikelS   s    
(r)   ��   z[37mUsername: �namez[37mEmail   : Zemailz[37mPhone   :Zphonez[37mBalance :r   z1[31mIsi config [33m'cfg.json' [31mdengan benarz[1;30mKeluar dari program....�   z1[31mFile [33m'cfg.json' [31mtidak ditemukan!!!z[31mPassword salah!!!)9Zdatetimer   r   Zurllib�rer   �osZorii�inputZaku�systemZbanner�round�aZfromtimestamp�br   �c�parseZquote�d�replace�e�openZbuk�loadr   r   ZbhZjsoZwallr   r   r$   �lenr   r   r%   Zvid�textZvidtZrvidZrvidt�findallr   Zrevid�extendr#   ZclisZclistr&   r)   r   Zstatus_code�KeyboardInterruptr   �FileNotFoundErrorr!   r!   r!   r"   �<module>   s�   8




