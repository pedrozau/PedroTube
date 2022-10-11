from flask import Flask, render_template,request,url_for
from pytube import YouTube,Playlist

'''
video.title # Title
video.video_id # Id
video.age_restricted # Age 
for video in playlist:
video.streams.get_highest_resolution().download()
'''

app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('down.html')

@app.route('/download',methods=['POST'])
def down():
    try:
        if request.method == "POST":
            url_video = request.form['url']
            if url_video == "":
                return "<script> alert('url video vazio')</script>"
            else:
                youtube = YouTube(url_video)
                video = youtube.streams.get_highest_resolution()
                video.download('./downloads')
                #titulo = youtube.title
                #id_video = youtube.video_id
                #datas = {'title':titulo,'video_id':id_video}
    except:
           return "Failha na conexão!!"

    return render_template('down.html'),200

@app.route('/play')
def playliste():
    return render_template('play.html'),200

@app.route('/playlist',methods=['POST'])
def playlist():
    try:
        if request.method == "POST":
            url = request.form['url']
            if url == "":
                return "<script> alert('url video vazio')</script>"
            else:
                playlist = Playlist(url)
                for video in playlist:
                    video.streams.get_highest_resolution().download('./downloads')
    except:
            return "Failha na conexão!!"
        
    return "download..."




if __name__ == "__main__":
    app.run(debug=True)
