import webbrowser

url = 'https://pythonexamples.org'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"))
webbrowser.get('chrome').open(url)
