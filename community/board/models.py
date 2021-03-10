from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('user.User',
                               on_delete=models.CASCADE,  # 사용자가 삭제되면 글도 삭제한다.
                               verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'
