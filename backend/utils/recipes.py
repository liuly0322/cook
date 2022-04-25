import jieba
import io

food_name = set()

f = io.open('utils/food_dict.txt')
food_name = { word.strip() for word in f.readlines() }
f.close()

def get_recipe_name(s: str) -> str:
    """
    s: 字符串
    输出：分词处理后得到的菜谱名
    """ 
    seg_list = jieba.cut(s)
    # prev: 考虑分词的容错
    prev, recipe_name, curr_recipe_name = '', '', ''
    for word in seg_list:
        if not curr_recipe_name and prev + word in food_name:
            word = prev + word
        if word in food_name:
            curr_recipe_name += word
            if len(curr_recipe_name) >= len(recipe_name):
                recipe_name = curr_recipe_name
        else:
            curr_recipe_name = ''
        prev = word
    return recipe_name
