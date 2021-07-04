import webbrowser

url = 'C:/Users/Manzar/OneDrive - Aga Khan University/R/programming/yesSir.mp3'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"))
webbrowser.get('chrome').open(url)
