from flask import Flask, render_template

app = Flask(__name__)

categories = {
    1: {
        "name": "مظلات مواقف السيارات",
        "details": "مظلات عالية الجودة تحمي سيارتك من العوامل الجوية.",
        "subcategories": [
            {"name": "مظلات حديد", "details": "متينة ومقاومة للعوامل الجوية.", "image": "2.jpg"},
            {"name": "مظلات خشبية", "details": "مظهر أنيق وتناسب الحدائق.", "image": "1.jpg"},
            {"name": "مظلات قماش PVC", "details": "مقاومة للماء والحرارة.", "image": "6.jpg"},
            {"name": "مظلات ألمنيوم", "details": "خفة وزن وقوة تحمل.", "image": "7.jpg"}
        ]
    },
    2: {
        "name": "المظلات، السواتر، وبيوت الشعر الملكي",
        "details": "تصاميم تجمع بين الفخامة والأصالة.",
        "subcategories": [
            {"name": "بيوت شعر فاخرة", "details": "مصممة بأعلى مستويات الفخامة.", "image": "3.jpg"},
            {"name": "سواتر خشبية", "details": "توفر الخصوصية والجمال.", "image": "2.jpg"},
            {"name": "سواتر حديد", "details": "قوية وتدوم طويلًا.", "image": "8.jpg"},
            {"name": "سواتر قماش", "details": "خفيفة وأنيقة.", "image": "9.jpg"},
            {"name": "بيوت شعر ملكية", "details": "تصاميم تقليدية فاخرة.", "image": "10.jpg"}
        ]
    },
    3: {
        "name": "المظلات المخروطية ومظلات الشد الإنشائي",
        "details": "تصاميم عصرية بأعلى جودة.",
        "subcategories": [
            {"name": "مظلات مخروطية", "details": "شكل فريد وجمالي.", "image": "4.jpg"},
            {"name": "مظلات شد إنشائي", "details": "مرونة وقوة تصميم.", "image": "5.jpg"},
            {"name": "مظلات PVC شد إنشائي", "details": "مقاومة عالية للظروف الجوية.", "image": "11.jpg"},
            {"name": "مظلات قماش شد إنشائي", "details": "أناقة وخفة وزن.", "image": "12.jpg"}
        ]
    },
    4: {
        "name": "مظلات الجلسات والبرجولات مع الألكسان",
        "details": "جلسات مريحة وتصميم حديث يناسب الأذواق.",
        "subcategories": [
            {"name": "برجولات خشبية", "details": "مناسبة للجلسات الخارجية.", "image": "4.jpg"},
            {"name": "برجولات ألكسان", "details": "شفافية وجمال متكامل.", "image": "1.jpg"},
            {"name": "مظلات جلسات قماش", "details": "توفر ظلًا مريحًا.", "image": "13.jpg"},
            {"name": "مظلات جلسات ألمنيوم", "details": "عصرية وقوية.", "image": "14.jpg"}
        ]
    },
    5: {
        "name": "الهناغر",
        "details": "تصاميم هندسية قوية مناسبة للمستودعات.",
        "subcategories": [
            {"name": "هناغر معدنية", "details": "متينة ومناسبة للتخزين.", "image": "2.jpg"},
            {"name": "هناغر حديدية", "details": "تدوم طويلًا مع قوة التحمل.", "image": "15.jpg"},
            {"name": "هناغر مستودعات", "details": "مساحات كبيرة للتخزين.", "image": "16.jpg"},
            {"name": "هناغر زراعية", "details": "تناسب الاستخدام الزراعي.", "image": "17.jpg"}
        ]
    }
}


@app.route('/')
def home():
    return render_template('index.html', categories=categories)

@app.route('/category/<int:category_id>')
def category(category_id):
    category = categories.get(category_id)
    if not category:
        return "القسم غير موجود", 404
    return render_template('category.html', category=category, category_id=category_id)

@app.route('/subcategory/<int:category_id>/<int:sub_id>')
def subcategory(category_id, sub_id):
    category = categories.get(category_id)
    if not category or sub_id >= len(category['subcategories']):
        return "الفرع غير موجود", 404
    subcategory = category['subcategories'][sub_id]
    return render_template('subcategory.html', subcategory=subcategory)
    
@app.route('/contact')
def contact():
    return render_template('contact.html')
    

if __name__ == '__main__':
    app.run(debug=True)