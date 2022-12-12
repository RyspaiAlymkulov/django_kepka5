# Generated by Django 4.1.4 on 2022-12-12 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_caps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagazineCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_cart_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_rate_caps', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MagazineDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_type', models.CharField(choices=[('Amount', 'amount'), ('Rate', 'rate')], default='rate', max_length=6)),
                ('discount_rate', models.IntegerField(blank=True, null=True)),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('minimum_purchased_items', models.IntegerField()),
                ('apply_to', models.CharField(choices=[('Caps', 'caps'), ('Category', 'category')], default='caps', max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('target_caps', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='custom_caps.caps')),
                ('target_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='custom_caps.category')),
            ],
        ),
    ]
