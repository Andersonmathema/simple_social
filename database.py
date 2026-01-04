import sqlite3
from sqlite3 import Connection
from typing import List
from models import Post, Posts

def get_post(connection:Connection)->Posts:
    with connection:
        cur = connection.cursor()
        cur.execute(
            '''
            SELECT post_title, post_text, user_id
            FROM posts;
            '''
        )
        return Posts(posts = [Post.model_validate(dict(post)) for post in cur])


def insert_post(connection: Connection, post : Post):
    with connection:
        cur = connection.cursor()
        cur.execute(
            '''
            INSERT INTO posts (post_title, post_text, user_id)
            VALUES(:post_title, :post_text, :user_id)
            ''',
            post.model_dump()
        )

if __name__ == '__main__':
    connection = sqlite3.connect('social.db')
    connection.row_factory = sqlite3.Row
    print(get_post(connection))
    #test_post = Post(post_title='Pydantic test', post_text='Another test', user_id=2)

    # test_post = {
    #     'post_title': 'First post',
    #     'post_text': 'This is a test',
    #     'user_id': 1
    # }
    #insert_post(connection, test_post)
    # for post in get_post(connection):
    #     print(dict(post))
    
'''git remote add origin https://github.com/Andersonmathema/simple_social.git
git branch -M main
git push -u origin main'''

