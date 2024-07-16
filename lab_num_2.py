def create_youtube_video(title, description):
	video = {"title": title,
	"description": description , 
	"likes": 0 , 
	"dislikes": 0 ,
	"comments":{"username":""}}
	return video

def like(youtube_video):
	if like in youtube_video:
		youtube_video["like"]+=1
	return youtube_video

def dislike(youtube_video):
	if dislikes in youtube_video:
		youtube_video["dislikes"]+=1
	return youtube_video

def add_comments(youtube_video, username, comment_text):
	if 'comments' not in youtube_video:
		youtube_video["comments"] = {}

	if username not in youtube_video["comments"]:
		youtube_video["comments"] [username] = []

	youtube_video["comments"][username].append(comment_text)
	return youtube_video

youtube_vid = create_youtube_video("How To Kiss" , "Lots Of Kissing")

youtube_vid = like(youtube_vid)
print ("likes are:" , youtube_vid)

youtube_vid = dislikes(youtube_vid)
print ("dislikes are:" , youtube_vid)

youtube_vid = add_comment(youtube_vid , "tommy23" , "Slay")
print("After you added the comment:" youtube_vid)

for i in range(495):
	youtube_vid = like(youtube_vid)

	print("Post likes:" , youtube_vid)
	# youtube_video["username"] = comment_text 
	# return comments




