from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)


class Blog(db.Model):
    __tablename__ = 'blog_posts'
    blog_id = db.Column(db.Integer, primary_key=True)
    featured_image = db.Column(db.String(300))
    post_by = db.Column(db.String(300))
    date = db.Column(db.String(300))
    tittle = db.Column(db.String(300))
    post = db.Column(db.String(300))
    meta_data = db.Column(db.String(300))

    def json(self):
        return {'tittle': self.tittle, 'post': self.post, 'featured_image': self.featured_image, 'post_by': self.post_by}

    def add_post(self, _tittle, _post, _featured_image, _post_by, _meta_data):
        new_blog = Blog(tittle=_tittle, post=_post, featured_image=_featured_image, post_by=_post_by, meta_data=_meta_data)
        db.session.add(new_blog)
        db.session.commit()

    def get_all_posts(self):
        return [Blog.json(blog)for blog in Blog.query.all(self)]

    def get_post(self, _blog_id):
        return Blog.json(Blog.query.filter_by(blog_id=_blog_id).first())

    def delete_post(self, _blog_id):
        Blog.query.filter_by(blog_id=_blod_id).delete()
        db.session.commit()

    def update_post_post(self, _blog_id, _post):
        post_to_update = Blog.query.filter_by(blod_id=_blog_id).first()
        post_to_update.post = _post
        db.session.commit()

    def replace_post(self, _blog_id, _post):
        post_to_replace = Blog.query.filter_by(blog_id=_blog_id).first()
        post_to_replace.post = _post
        db.session.commit()

    def __repr__(self):
        blog_object = {
            'tittle': self.tittle,
            'featured_image': self.featured_image,
            'post': self.post,
            'post_by': self.post_by
        }
        return json.dumps(blog_object)