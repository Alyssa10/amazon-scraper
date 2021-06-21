product_urls = ["https://www.amazon.com/Logitech-Wireless-Lightspeed-Headset-Headphone/product-reviews/B081PP4CB6/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="]
number_of_pages_to_scrape = 100
with open("urls.txt", "w") as text_file:
    for product_url in product_urls:
        for page_num in range(1, number_of_pages_to_scrape+1):  
            url = f"{product_url}{page_num}\n"
            print(url)
            text_file.write(url)
