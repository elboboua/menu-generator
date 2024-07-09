from menu_generator import MenuGeneratorFactory, BusinessInfo

mg = MenuGeneratorFactory().create_menu_generator()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ =='__main__':
    business_name = input(f"{bcolors.HEADER}Enter the name of the business: {bcolors.ENDC}")
    business_description = input(f"{bcolors.HEADER}Enter a description of the business: {bcolors.ENDC}")
    business_city = input(f"{bcolors.HEADER}Enter the city where the business is located: {bcolors.ENDC}")
    business_cost_level = int(input(f"{bcolors.HEADER}Enter the cost level of the business (1-5): {bcolors.ENDC}"))
    
    business_info = BusinessInfo(name=business_name, description=business_description, city=business_city, cost_level=business_cost_level)
    
    mg = MenuGeneratorFactory().create_menu_generator()
    
    categories = mg.generate_categories(business_info)
    for category in categories:
        print(bcolors.OKGREEN, f"{category.name}: {category.description}", bcolors.ENDC)
        items = mg.generate_items(category, business_info)
        for item in items:
            print("\t", bcolors.OKCYAN ,f"{item.name}: {item.description} {item.price}", bcolors.ENDC)