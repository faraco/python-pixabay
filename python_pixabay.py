from requests import get

class Pixabay:
    """
        @brief Handle Pixabay video and image searches
    """

    def __init__(self, api_key):
        """Constructor
           @param api_key <b>str</b> Your Pixabay API key.
           @see https://pixabay.com/en/accounts/register/ to register and get an API key.
           
           @param root_url: URL for Pixabay API
        """
        self.api_key = api_key
        self.root_url = "https://pixabay.com/api/"

    def image_search(self, q='yellow flower', lang='en', id='',
                           response_group='image_details',
                           image_type='all',
                           orientation='all',
                           category='',
                           min_width=0,
                           min_height=0,
                           editors_choice='false',
                           safesearch='false',
                           order='popular',
                           page=1,
                           per_page=20,
                           callback='',
                           pretty='false'):
        """
            Image search
            @brief Search for Pixabay images using default arguments if no <b>optional</b> arguments supplied.
            @param q <b>str</b> A URL encoded search term. If omitted, all images are returned. This value may not exceed 100 characters.<br>
            Example: "cat dog"<br>
            Default: "yellow flower"
    
            @param lang <b>str</b> Language code of the language to be searched in.<br>
            Accepted values: cs, da, de, en, es, fr, id, it, hu, nl, no, pl, pt, ro, sk, fi, sv, tr, vi, th, bg, ru, el, ja, ko, zh <br>
            Default: "en"
    
            @param id <b>str</b> ID, hash ID, or a comma separated list of values for retrieving specific images.<br>
            In a comma separated list, IDs and hash IDs cannot be used together.<br>
            Default: " "
    
            @param response_group <b>str</b> Choose between retrieving high resolution images and image details.<br>
            When selecting details, you can access images up to a dimension of 960 x 720 px.<br>
            Accepted values: "image_details", "high_resolution" (requires permission)<br>
            Default: "image_details"
    
            @param image_type <b>str</b> Filter results by image type.<br>
            Accepted values: "all", "photo", "illustration", "vector"<br>
            Default: "all"
    
            @param orientation <b>str</b> Whether an image is wider than it is tall, or taller than it is wide.<br>
            Accepted values: "all", "horizontal", "vertical"<br>
            Default: "all" 
    
            @param category <b>str</b>  Filter results by category. <br>
            Accepted values: fashion, nature, backgrounds, science, education, people, feelings, religion, health, places, animals, industry, food, computer, sports, transportation, travel, buildings, business, music <br>
            Default: " "

            @param min_width <b>int</b> Minimum image width. <br>
            Default: 0
    
            @param min_height <b>int</b> Minimum image height. <br>
            Default: 0

            @param editors_choice <b>bool</b> Select images that have received an Editor's Choice award.<br>
            Accepted values: "true", "false"<br>
            Default: "false" 
    
            @param safesearch <b>bool</b> A flag indicating that only images suitable for all ages should be returned.<br>
            Accepted values: "true", "false"<br>
            Default: "false" 
    
            @param order <b>str</b> How the results should be ordered. <br>
            Accepted values: "popular", "latest" <br>
            Default: "popular" 
    
            @param page <b>int</b> Returned search results are paginated. Use this parameter to select the page number. <br>
            Default: 1 
    
            @param per_page <b>int</b> Determine the number of results per page.<br>
            Accepted values: 3 - 200 <br>
            Default: 20 
    
            @param callback <b>string</b> JSONP callback function name<br>
            Default: " "
     
            @param pretty <b>bool</b> Indent JSON output. This option should not be used in production.<br>
            Accepted values: "true", "false"<br>
            Default: "false" 
    
            @return Image search data in JSON format.
        """

        payload = {'key': self.api_key, 'q': q, 'lang': lang, 'id': id,
                'response_group': response_group, 'image_type': image_type,
                'orientation': orientation, 'category': category,
                'min_width': min_width, 'min_height': min_height,
                'editors_choice': editors_choice, 'safesearch': safesearch,
                'order': order, 'page': page, 'per_page': per_page,
                'callback': callback, 'pretty': pretty
                }
        
        resp = get(self.root_url, params=payload)
        #return the json object if the API call is successful, otherwise raise an error with the raw response with the HTTP status code
        if resp.status_code == 200:
            return resp.json()
        else:
            raise ValueError(resp.text)

    def video_search(self, q='yellow flower',
                           lang='en',
                           id='',
                           video_type='all',
                           category='',
                           min_width=0,
                           min_height=0,
                           editors_choice='false',
                           safesearch='false',
                           order='popular',
                           page=1,
                           per_page=20,
                           callback='',
                           pretty='false'):
        """
            Video search
            @brief Search for Pixabay video using default arguments if no <b>optional</b> arguments supplied.
            @param q <b>str</b> A URL encoded search term. If omitted, all images are returned. This value may not exceed 100 characters.<br>
            Example: "cat dog"<br>
            Default: "yellow flower"
    
            @param lang <b>str</b> Language code of the language to be searched in.<br>
            Accepted values: cs, da, de, en, es, fr, id, it, hu, nl, no, pl, pt, ro, sk, fi, sv, tr, vi, th, bg, ru, el, ja, ko, zh <br>
            Default: "en"
    
            @param id <b>str</b> ID, hash ID, or a comma separated list of values for retrieving specific images.<br>
            In a comma separated list, IDs and hash IDs cannot be used together.<br>
            Default: " "
    
            @param video_type <b>str</b> Filter results by video type. <br>
            Accepted values: "all", "film", "animation"<br>
            Default: "all" 
    
            @param category <b>str</b>  Filter results by category. <br>
            Accepted values: fashion, nature, backgrounds, science, education, people, feelings, religion, health, places, animals, industry, food, computer, sports, transportation, travel, buildings, business, music <br>
            Default: " "

            @param min_width <b>int</b> Minimum image width. <br>
            Default: 0
    
            @param min_height <b>int</b> Minimum image height. <br>
            Default: 0

            @param editors_choice <b>bool</b> Select images that have received an Editor's Choice award.<br>
            Accepted values: "true", "false"<br>
            Default: "false" 
    
            @param safesearch <b>bool</b> A flag indicating that only images suitable for all ages should be returned.<br>
            Accepted values: "true", "false"<br>
            Default: "false" 
    
            @param order <b>str</b> How the results should be ordered. <br>
            Accepted values: "popular", "latest" <br>
            Default: "popular" 
    
            @param page <b>int</b> Returned search results are paginated. Use this parameter to select the page number. <br>
            Default: 1 
    
            @param per_page <b>int</b> Determine the number of results per page.<br>
            Accepted values: 3 - 200 <br>
            Default: 20 
    
            @param callback <b>string</b> JSONP callback function name<br>
            Default: " "
     
            @param pretty <b>bool</b> Indent JSON output. This option should not be used in production.<br>
            Accepted values: "true", "false"<br>
            Default: "false" 
    
            @return Video search data in JSON format.
        """

        payload = {'key': self.api_key, 'q': q, 'lang': lang, 'id': id,
                'video_type': video_type,
                'category': category,
                'min_width': min_width, 'min_height': min_height,
                'editors_choice': editors_choice, 'safesearch': safesearch,
                'order': order, 'page': page, 'per_page': per_page,
                'callback': callback, 'pretty': pretty}

        resp = get(self.root_url + "videos/", params=payload)
        if resp.status_code == 200:
            return resp.json()
        else:
            raise ValueError(resp.text)

