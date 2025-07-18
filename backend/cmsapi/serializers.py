from rest_framework import serializers
from .models import Article, Category
from users.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.EmailField(required=True, write_only=True)
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    author_name = serializers.SerializerMethodField(read_only=True)
    author_email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'summary',
            'status',
            'published_date',
            'categories',
            'author',
            'author_name',
            'author_email',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_author_name(self, obj):
        return obj.author.name if obj.author else None

    def get_author_email(self, obj):
        return obj.author.email if obj.author else None

    def validate_author(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Author does not exist.")
        return value

    def create(self, validated_data):
        categories = validated_data.pop('categories')
        author_email = validated_data.pop('author')
        user = User.objects.get(email=author_email)
        article = Article.objects.create(author=user, **validated_data)
        article.categories.set(categories)
        return article

    def update(self, instance, validated_data):
        validated_data.pop('author', None)
        categories = validated_data.pop('categories', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if categories is not None:
            instance.categories.set(categories)

        instance.save()
        return instance
