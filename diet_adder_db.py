from dbDiet import dbDiet

title_string = """
 __    __  __    __  ________  _______   ______        _______   _______  
/  \  /  |/  |  /  |/        |/       \ /      |      /       \ /       \ 
$$  \ $$ |$$ |  $$ |$$$$$$$$/ $$$$$$$  |$$$$$$/       $$$$$$$  |$$$$$$$  |
$$$  \$$ |$$ |  $$ |   $$ |   $$ |__$$ |  $$ | ______ $$ |  $$ |$$ |__$$ |
$$$$  $$ |$$ |  $$ |   $$ |   $$    $$<   $$ |/      |$$ |  $$ |$$    $$< 
$$ $$ $$ |$$ |  $$ |   $$ |   $$$$$$$  |  $$ |$$$$$$/ $$ |  $$ |$$$$$$$  |
$$ |$$$$ |$$ \__$$ |   $$ |   $$ |  $$ | _$$ |_       $$ |__$$ |$$ |__$$ |
$$ | $$$ |$$    $$/    $$ |   $$ |  $$ |/ $$   |      $$    $$/ $$    $$/ 
$$/   $$/  $$$$$$/     $$/    $$/   $$/ $$$$$$/       $$$$$$$/  $$$$$$$/  
                    Welcome to Nutri-DB
                    by Héctor Miranda García

Thi is a simple tool that enables you to keep record of your daily diet.
It adds the data to a simple csv data_base. Its intended for data Science
projects. The dbDiet class contains a series of functions that makes it
easy.
\n                                                            
"""
print()
x = dbDiet()
x.automatic()