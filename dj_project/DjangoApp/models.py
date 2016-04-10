from DjangoApp.import_files.model_models import *
# from django.conrtib.comments.models import Comment


#customize user table add feild,so make new table with relations
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='static/images/user', blank=True)
	# USER_TYPES = Choices('Regular', 'Editor','Admin')
	# user_type = models.CharField(choices=USER_TYPES, max_length=50)
	def __unicode__(self):
		return unicode(self.user)

class Customer(User):
	class Meta:
		proxy = True
		app_label = 'auth'
		verbose_name = 'User account'
		verbose_name_plural = 'User accounts'

class Tag(models.Model):
    tag_title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.tag_title


class Article(models.Model):
	subject = models.CharField(max_length=150)
	description = models.TextField()
	image = models.ImageField(upload_to='static/images/article', blank=True ,null=True)
	date = models.DateTimeField(default=datetime.now())
	is_publish = models.BooleanField(default=False)
	is_denied = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag ,null=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL) 
	veiw_count = CounterField()
	comment_count =CounterField()
	def __unicode__(self):
		return self.subject

	# class Meta:
	# 	permissions = (
	# 		("is_publish", "is_publish")
	# 	)
	

class Comment(CounterMixin, models.Model):
	content=models.CharField(max_length=500)
	date=models.DateTimeField(default=datetime.now())
	Article_comment_id= models.ForeignKey(Article,on_delete=models.CASCADE)
	reply = models.ForeignKey('self', null=True, related_name='replies')
	def __unicode__(self):
		return self.content
	def __str__(self):
		return self.content



# class like(models.Models):
	
class emotion(models.Model):
	photo=models.CharField(max_length=100)
	Comment_emotion_id= models.ForeignKey(Comment,on_delete=models.CASCADE)


class banWords(models.Model):
	word = models.CharField(max_length=100 , unique=True)
	def __unicode__(self):
		return self.word


class like(models.Model):
	User_like_id= models.ForeignKey(User,on_delete=models.CASCADE)
	is_like = models.BooleanField(default=False)
	Comment_like_id=models.ForeignKey(Comment,on_delete=models.CASCADE)

class mark(models.Model):
	User_mark_id= models.ForeignKey(User,on_delete=models.CASCADE)
	is_mark = models.BooleanField(default = False)
	Article_mark_id=models.ForeignKey(Comment,on_delete=models.CASCADE)

class LockSystem(models.Model):
	Name = models.CharField(max_length=100 , default="Blog System")
	is_lock = models.BooleanField(default=False)

# admin.site.register(LockSystem)
# admin.site.register(emotion)
admin.site.register(banWords)