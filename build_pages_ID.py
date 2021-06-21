product_codes = ["B07NSN41YB"]
number_of_pages_to_scrape = 10
with open("urls.txt", "w") as text_file:
    for product_code in product_codes:
        for page_num in range(1, number_of_pages_to_scrape+1):  
            product_url = f"https://www.amazon.com/product-reviews/{product_code}/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
            url = f"{product_url}{page_num}\n"
            print(url)
            text_file.write(url)
