# Generated by Django 3.0.3 on 2023-08-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videobasesetting',
            options={'verbose_name': '视频基本设置', 'verbose_name_plural': '视频基本设置'},
        ),
        migrations.AlterField(
            model_name='videobasesetting',
            name='frame_set',
            field=models.CharField(choices=[('设置抽帧', '设置抽帧'), ('不设置抽帧', '不设置抽帧')], default='', max_length=20, verbose_name='抽帧设置'),
        ),
        migrations.AlterField(
            model_name='videobasesetting',
            name='hqdn3d_chroma_spatia',
            field=models.FloatField(default=1.5, help_text='较大的值会增加降噪效果', verbose_name='色度通道降噪强度'),
        ),
        migrations.AlterField(
            model_name='videobasesetting',
            name='hqdn3d_luma_spatial',
            field=models.FloatField(default=1.5, help_text='较大的值会增加降噪效果', verbose_name='空间降噪强度'),
        ),
    ]
