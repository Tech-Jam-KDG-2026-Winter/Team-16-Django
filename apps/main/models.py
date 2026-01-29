from django.db import models
from django.contrib.auth.models import User

# ------------------------
# プロフィール拡張
# ------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='profile_icons/', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.nickname or self.user.username


# ------------------------
# 運動記録（投稿）
# ------------------------
class ExercisePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    duration = models.IntegerField(help_text="運動時間（分）")
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"


# ------------------------
# いいね（リアクション）
# ------------------------
class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        ExercisePost,
        on_delete=models.CASCADE,
        related_name='reactions'
    )

    class Meta:
        unique_together = ('user', 'post')


# ------------------------
# フォロー機能
# ------------------------
class Follow(models.Model):
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers'
    )

    class Meta:
        unique_together = ('follower', 'following')


# ------------------------
# 管理者用情報（BANなど）
# ------------------------
class AdminUserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)  # 停止/有効
    ban_reason = models.TextField(blank=True, null=True)
    banned_at = models.DateTimeField(null=True, blank=True)
    banned_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='banned_users'
    )

    def __str__(self):
        return self.user.username
