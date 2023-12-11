# streamlit run test.py

import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import pickle
smb_raw = pd.read_csv('smb_restaurants - dataset.csv')
st.set_page_config(layout="wide")

def embed(embed_code, platform):
    st.markdown(embed_code, unsafe_allow_html=True)

def main():
    st.title("Social Media Embeds with Streamlit")

    # Replace these URLs with the actual URLs of the TikTok, Instagram, and Facebook content you want to embed
    # tiktok_url = '<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@spoon_northeastern/video/7164849465260559658" data-video-id="7164849465260559658" data-embed-from="embed_page" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@spoon_northeastern" href="https://www.tiktok.com/@spoon_northeastern?refer=embed">@spoon_northeastern</a> <p>@salonikigreek now has a new location on newbury st! <a title="bostonfood" target="_blank" href="https://www.tiktok.com/tag/bostonfood?refer=embed">#bostonfood</a> <a title="bostonfoodies" target="_blank" href="https://www.tiktok.com/tag/bostonfoodies?refer=embed">#bostonfoodies</a> <a title="fyp" target="_blank" href="https://www.tiktok.com/tag/fyp?refer=embed">#fyp</a></p> <a target="_blank" title="♬ original sound - Spoon Northeastern" href="https://www.tiktok.com/music/original-sound-7164849472009161514?refer=embed">♬ original sound - Spoon Northeastern</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>'
    # instagram_url = '<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/reel/Cz2GVmHsmSt/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/reel/Cz2GVmHsmSt/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/reel/Cz2GVmHsmSt/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by Saloniki Greek (@salonikigreek)</a></p></div></blockquote> <script async src="//www.instagram.com/embed.js"></script>'
    # facebook_url = ''

    # bootstrap 4 collapse example
    components.html(
    """
    <div class="row">
    <div class="column">
        
    </div>
    <div class="column">
            
    </div>
    <div class="column"></div>
    </div>
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Social Media Embeds</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            .container {
                display: flex;
                justify-content: space-around;
                align-items: flex-start;
                padding: 20px;
            }
            .column {
                flex: 1;
                margin: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Column 1: TikTok Embed -->
            <div class="column">
                <h2>TikTok Video</h2>
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@salonikigreek/video/7236772909220515118" data-video-id="7236772909220515118" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@salonikigreek" href="https://www.tiktok.com/@salonikigreek?refer=embed">@salonikigreek</a> <p>Foolproof way to improve your week: Grab yourself some Saloniki 🙌</p> <a target="_blank" title="♬ original sound  - Saloniki Greek" href="https://www.tiktok.com/music/original-sound-Saloniki-Greek-7236772913410624298?refer=embed">♬ original sound  - Saloniki Greek</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>                <script async src="https://www.tiktok.com/embed.js"></script>
            </div>

            <!-- Column 2: Instagram Embed -->
            <div class="column">
                <h2>Instagram Video</h2>
                <blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/reel/Cz2GVmHsmSt/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/reel/Cz2GVmHsmSt/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/reel/Cz2GVmHsmSt/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by Saloniki Greek (@salonikigreek)</a></p></div></blockquote> 
                <script async src="//www.instagram.com/embed.js"></script>
            </div>

            <!-- Column 3: Facebook Embed -->
            <div class="column">
                <h2>Facebook Post</h2>
<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fsalonikigreek%2Fposts%2Fpfbid02BTAJnMQxRcY7vTLJSdijf1VSPc3GELjDCvHBBXp3LywgPrEA2yLeX1etKiVYbbAWl&show_text=true&width=500" width="500" height="793" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>            </div>
        </div>
    </body>
    </html>

    """,
    height = 1600
    )

def preprocess_smb_data(smb_raw):
    smb = smb_raw.replace('na', np.nan)
    # Assuming your DataFrame is df
    smb.fillna(0, inplace=True)
    data_types = {'business_name': 'string', 'insta_link': 'string', 'insta_name': 'string', }
    smb = smb.astype(data_types)
    strtype_colnames = {"business_name", "insta_link", "insta_name", "fb_link", "insta_name.1", "Unnamed: 41", "tiktok_link"}
    numeric_features = set(smb.columns) - strtype_colnames
    for feature in numeric_features:
        smb[feature] = smb[feature].replace(',', '', regex=True)
        smb[feature] = pd.to_numeric(smb[feature], errors='coerce')

    return smb


def plot_histogram(restaurant_name, smb):
    smb_copy = smb.copy()
    smb_copy.loc[len(smb_copy)] = {
        "business_name": restaurant_name,
        "insta_followers": num_followers
    }

    # Filter data for insta_followers less than 20000
    filtered_data = smb_copy[smb_copy['insta_followers'] < 20000]['insta_followers']
    
    # Create a figure and subplots
    fig, axs = plt.subplots()

    # Plot the histogram with clear borders
    n, bins, patches = axs.hist(filtered_data, bins=30, color='gray', alpha=0.7, edgecolor='black')
    #sns.kdeplot(filtered_data, color='blue', ax=axs, label='Density Curve')
    axs.set_xlabel('Instagram Followers')
    axs.set_ylabel('Frequency')
    axs.set_title('Distribution of Instagram Followers in the Boston Area')

    # Find the percentile of the data point
    percentile = (np.sum(filtered_data <= num_followers) / len(filtered_data)) * 100

    # Annotate the percentile on the plot
    data_point = smb_copy.loc[len(smb_copy)-1]
    axs.vlines(x=data_point['insta_followers'], ymin=0, ymax=max(n), colors='yellow', linestyles='dashed')
    axs.annotate(f'Percentile: {percentile:.2f}%', xy=(data_point['insta_followers'], max(n)/2), 
                 xytext=(data_point['insta_followers'] + 1000, max(n)/2*1.6), arrowprops=dict(facecolor='black', shrink=0.05))

    # Display the plot
    st.pyplot(fig)

with open('model_result/insta_model_like.pkl', 'rb') as file:
    insta_model_like = pickle.load(file)

with open('model_result/insta_model_comment.pkl', 'rb') as file:
    insta_model_comment = pickle.load(file)

with open('model_result/insta_model_view.pkl', 'rb') as file:
    insta_model_view = pickle.load(file)

with open('model_result/fb_model_like.pkl', 'rb') as file:
    fb_model_like = pickle.load(file)

with open('model_result/fb_model_comment.pkl', 'rb') as file:
    fb_model_comment = pickle.load(file)

with open('model_result/tiktok_biz_model_like.pkl', 'rb') as file:
    tiktok_biz_model_like = pickle.load(file)

with open('model_result/tiktok_biz_model_comment.pkl', 'rb') as file:
    tiktok_biz_model_comment = pickle.load(file)

with open('model_result/tiktok_nonbiz_model_like.pkl', 'rb') as file:
    tiktok_nonbiz_model_like = pickle.load(file)

with open('model_result/tiktok_nonbiz_model_comment.pkl', 'rb') as file:
    tiktok_nonbiz_model_comment = pickle.load(file)
    
with open('model_result/tiktok_nonbiz_model_view.pkl', 'rb') as file:
    tiktok_nonbiz_model_view = pickle.load(file)

text_input_container = st.empty()
text_input_container.text_input("Enter your restaurant's name", key="text_input")

if st.session_state.text_input != "":
    text_input_container.empty()
    st.title(f"Hello, **{st.session_state.text_input}!**")

name = st.session_state.text_input

col1, col2 = st.columns(2)


with col1:
    file = st.file_uploader("Upload a file with last month of views, comments and like on Instagram, Facebook and Tiktok")
    if file:
        df = pd.read_csv(file)

        insta_like_pred = insta_model_like.predict(df)
        insta_comment_pred = insta_model_comment.predict(df)
        insta_view_pred = insta_model_view.predict(df)
        fb_like_pred = fb_model_like.predict(df)
        fb_comment_pred = fb_model_comment.predict(df)
        tiktok_biz_like_pred = tiktok_biz_model_like.predict(df)
        tiktok_biz_comment_pred = tiktok_biz_model_comment.predict(df)
        tiktok_nonbiz_like_pred = tiktok_nonbiz_model_like.predict(df)
        tiktok_nonbiz_comment_pred = tiktok_nonbiz_model_comment.predict(df)
        tiktok_nonbiz_view_pred = tiktok_nonbiz_model_view.predict(df)

        print("insta_view_pred", insta_view_pred)
        st.markdown("**Prediction Result:**")
        column_names = ['Instagram', 'Facebook', 'Tiktok business', 'Tiktok non-business']
        row_names = ['View', 'Like', 'Comment']

        dict_val = {
            'insta_like_range_month_m':{
                1:'(-0.001, 13.95]'
                , 2:'(13.95, 67.2]'
                , 3:'(67.2, 181.1]'
                , 4:'(181.1, 7864.8]'
            }
            , 'insta_view_range_month_m':{
                1:'(-0.001, 2083.75]'
                , 2:'(2083.75, 359000.0]'
            }
            , 'insta_comment_range_month_m':{
                1:'(-0.001, 2.0]'
                , 2:'(2.0, 7.0]'
                , 3:'(7.0, 3329.0]' 
            }
            , 'fb_like_range_month_m':{
                1:'(-0.001, 0.4]'
                , 2:'(0.4, 6.2]'
                , 3:'(6.2, 4610.6]' 
            }
            , 'fb_comment_range_month_m':{
                1:'(-0.001, 0.2]'
                , 2:'(0.2, 110.2]'
            }
            , 'tiktok_biz_like_range_month_m':{
                1:'(-0.001, 11.3]'
                , 2:'(11.3, 47.312]'
                , 3:'(47.312, 3329.6]' 
            }
            , 'tiktok_biz_comment_range_month_m':{
                1:'(-0.001, 0.688]'
                , 2:'(0.688, 5562.6]'
            }
            , 'tiktok_nonbiz_like_range_month_m':{
                1:'(-0.001, 2.5]'
                , 2:'(2.5, 61.25]'
                , 3:'(61.25, 31200.0]'
            }
            , 'tiktok_nonbiz_view_range_month_m':{
                1:'(-0.001, 256.625]'
                , 2:'(256.625, 1633.0]'
                , 3:'(1633.0, 408000.0]'
            }
            , 'tiktok_nonbiz_view_range_month_m':{
                1:'(-0.001, 256.625]'
                , 2:'(256.625, 1633.0]'
                , 3:'(1633.0, 408000.0]'
            }
            , 'tiktok_nonbiz_comment_range_month_m':{
                1:'(-0.001, 2.0]'
                , 2:'(2.0, 197.0]'
            }
        }

        # Create an empty DataFrame with specified column names
        result_table_df = pd.DataFrame(columns=column_names, index=row_names)

        # Function to get the range from dict_val based on prediction
        def get_range(pred, key):
            print("pred,key", pred, key)
            return dict_val[key].get(pred, 'N/A')

        # Extract the range based on the predictions and fill the DataFrame
        result_table_df.loc['View', 'Instagram'] = get_range(insta_view_pred[0], 'insta_view_range_month_m')
        result_table_df.loc['Like', 'Instagram'] = get_range(insta_like_pred[0][0], 'insta_like_range_month_m')
        result_table_df.loc['Comment', 'Instagram'] = get_range(insta_comment_pred[0][0], 'insta_comment_range_month_m')

        result_table_df.loc['View', 'Facebook'] = 'N/A'  # Assuming no prediction available
        result_table_df.loc['Like', 'Facebook'] = get_range(fb_like_pred[0][0], 'fb_like_range_month_m')
        result_table_df.loc['Comment', 'Facebook'] = get_range(fb_comment_pred[0], 'fb_comment_range_month_m')

        result_table_df.loc['View', 'Tiktok business'] = 'N/A'  # Assuming no prediction available
        result_table_df.loc['Like', 'Tiktok business'] = get_range(tiktok_biz_like_pred[0][0], 'tiktok_biz_like_range_month_m')
        result_table_df.loc['Comment', 'Tiktok business'] = get_range(tiktok_biz_comment_pred[0], 'tiktok_biz_comment_range_month_m')

        result_table_df.loc['View', 'Tiktok non-business'] = get_range(tiktok_nonbiz_view_pred[0][0], 'tiktok_nonbiz_view_range_month_m')
        result_table_df.loc['Like', 'Tiktok non-business'] = get_range(tiktok_nonbiz_like_pred[0][0], 'tiktok_nonbiz_like_range_month_m')
        result_table_df.loc['Comment', 'Tiktok non-business'] = get_range(tiktok_nonbiz_comment_pred[0], 'tiktok_nonbiz_comment_range_month_m')

        
        st.table(result_table_df)

        st.markdown("**Our recommendation:**")
        ####
        st.markdown("Spend **:blue[162%]** more time creating contents on **Tiktok**")
        st.markdown("Spend :red[17%] less time creating contents on **Instagram**")
        st.markdown("Spend :red[86%] less time creating contents on **Facebook**")
        ####


with col2:
    #st.text("Let us know you current follower count :)")
    # text_input_container1 = st.empty()
    # text_input_container1.text_input("Enter your restaurant's name") #key="text_input")


# Placeholder values
    default_comments = 0
    default_views = 0
    default_likes = 0
    default_followers = 0

# Input boxes for Number of Comments, Views, and Likes
    num_followers = st.number_input("Enter your current Instagram follower count", value=default_followers)
# num_comments = st.number_input("Number of Comments", value=default_comments)
# num_views = st.number_input("Number of Views", value=default_views)
# num_likes = st.number_input("Number of Likes", value=default_likes)

# # Display the entered values
# st.write(f"Number of Followers: {num_followers}")
# st.write(f"Number of Comments: {num_comments}")
# st.write(f"Number of Views: {num_views}")
# st.write(f"Number of Likes: {num_likes}")

# # Display number input boxes with half width
# col1, col2 = st.columns(2)

# with col1:
#     number_of_comments = st.number_input("Number of Comments")

# with col2:
#     number_of_views = st.number_input("Number of Views")
 
# The third box takes the full width of the page
# number_of_likes = st.number_input("Number of Likes")

# You can customize the width by adjusting the column width
    if num_followers:

        st.markdown("**Let's see how you compare to other restaurants in the Boston Area**")

        smb = preprocess_smb_data(smb_raw)


        plot_histogram("", smb)



if __name__ == "__main__" and name:
    main()