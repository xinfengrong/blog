# 视图模块
import hashlib
from random import randint

from flask_login import login_required

from App.SMS import sms
from App.blog import *
from App.ext import db
from flask import Blueprint, render_template, request, redirect, session, make_response, jsonify
from App.form import *
from App.verifycode import vc

blog = Blueprint('blog', __name__)


@blog.route('/')
def home():
    # 查询文章数据
    articles = Article.query.all()
    user = User.query.first()
    # 找到需要修改的位置，把内容替换进去
    # 渲染数据
    return render_template('index.html', **locals())


@blog.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            phone = form.phone.data
            password = form.password.data
            user = User(username=username)
            user.password = hashlib.sha1(password.encode('utf-8')).hexdigest()
            user.phone=phone
            db.session.add(user)
            db.session.commit()
            return redirect('/')

    return render_template('register.htm', **locals())


@blog.route('/verify/')
def verify_code():
    result = vc.generate()
    session['code'] = vc.code
    response = make_response(result)
    response.headers['Content-Type'] = 'image/png'
    return response

#先测试路由--注册写个jquery---查jquery在线手册
@blog.route('/send/', methods=['POST', 'GET'])
def send_sms():
    # if request.method=='POST':
    phone = request.values.get('phone')
    # print(phone)
    # phone='15071348670'
    if phone:
        # 产生一个随机验证码
        num = randint(1000,9999)
        # 添加到session中，将来与用户输入比较
        session['sms'] = str(num)
        para = "{'code':'%d'}" % num  # 必须是json字符串
        res = sms.send(phone, para)
        print(res, type(res))
        return jsonify({'code': 1, 'msg': 'chenggong'})
    return jsonify({'code': 0, 'msg': 'no phone'})


# 博文分类展示----观察页面特点得知，是一个博文分类展示页面，内容是动态生成的
@blog.route('/list/')
@blog.route('/list/<int:cid>/')
# @blog.route('/list/<int:page>/')
def list_article(cid=1):  # 如果分类号不给的话，默认就是1
    if cid < 0:  # 如果不带参数cid，值是-1，就查询默认分类
        # 获取默认分类中的所有文章
        # 两表联合查询，可以不用外键
        category = Category.query.first()
        # 最好先打印一下看看得到的是什么，在还没有那么熟练的情况下！！！
        # print(category)  # <Category 1>  是一个对象
        cid = category.cid
    # 大于等于0，查指定分类
    articles = db.session.query(Article, Category).filter(Article.cid == Category.cid, Category.cid == cid).all()
    # print(articles)  # [(<Article 1>, <Category 1>)] ---需要把数据显示到blog上
    article_num = len(articles)
    # print(article_num)

    # 提取分类数据
    categories = Category.query.all()  # [<Category 1>, <Category 2>, <Category 3>, <Category 4>]
    # print(categories)

    # 最近三篇文章
    three_articles = Article.query.order_by(-Article.create_time).all()[:3]
    # print(three_articles) #[<Article 1>, <Article 2>, <Article 3>]

    # 获取标签
    tags = Tag.query.all()[:4]

    user = User.query.first()

    page=1
    pagination = Article.query.paginate(page, 2)
    # for page in pagination.pages:
    #     pagination1=Article.query.paginate(page,2)
    # for i in pagination.iter_pages():
        # print(i)
    # print(pageination.__dict__)  #{'query': <flask_sqlalchemy.BaseQuery object at 0x00000000052BFBA8>, 'page': 1, 'per_page': 2, 'total': 9, 'items': [<
#Article 1>, <Article 2>]}


    return render_template('blog.html', **locals())


# 分页
# @blog.route('/pages/')
@blog.route('/list/<int:page>/')
def page_blog(page=1):
    # if page<0:
    #     pagination = Article.query.paginate(1, 2)
    # pagination=Article.query.paginate(page, 2)
    # print(pageination.__dict__)
    return redirect('/list/')
    # return render_template('blog.html',**locals())


@blog.route('/post/')
@blog.route('/post/<int:aid>')
@login_required
def post_articles(aid=1):
    if aid < 0:
        # 获取文章详情
        # category = Category.query.first()
        # cid = category.cid
        article = Article.query.first()
        aid = article.aid
    article = Article.query.get(aid)
    cid = article.cid
    category1 = Category.query.get(cid)
    tag1 = Tag.query.get(aid)

    # print(articles)
    tags = db.session.query(Tag, Article).filter(Article.aid == Tag.aid, Article.aid == aid).all()
    tag_num = len(tags)

    # articles = db.session.query(Article, Category).filter(Article.cid == Category.cid, Category.cid == cid).all()
    # print(articles) #[(<Article 1>, <Category 1>), (<Article 5>, <Category 1>), (<Article 6>, <Category 1>),
    # (<Article 7>, <Category 1>), (<Article 8>, <Category 1>)]
    # article_num = len(articles)
    # print(articles[0][0].picture)
    # 获取作者
    user = User.query.first()

    # print(data)
    # print(user.username)  如果是列表的话，不可以这样直接取，因为all得到的是列表
    # print(user.portrait)
    # print(user)

    # 获取最近3篇文章
    three_articles = Article.query.order_by(-Article.create_time).all()[:3]
    categories = db.session.query(Category, Article).filter(Article.cid == Category.cid, Article.aid == aid).all()
    # print(categories) #[(<Category 1>, <Article 1>)]
    category_num = len(categories)
    for i in range(0, category_num):
        # article=categories[i][0].articles
        # print(article)
        articles1 = categories[i][0].articles.first()
        aid1 = articles1.aid
        print(aid1)
        # print(categories[i][0].articles.all())
        # print(categories[i]) #(<Category 1>, <Article 1>)
    # 获取分类类别
    categories = Category.query.all()

    # 获取标签
    tags = Tag.query.all()[:4]

    # 获取最新三篇评论
    marks = Mark.query.order_by(-Mark.create_time).all()[:3]

    # 获取文章总数
    articles2 = Article.query.all()
    num = len(articles2)


    return render_template('post.html', **locals())





