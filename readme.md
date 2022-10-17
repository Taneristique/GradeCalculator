# How To Use Grade Calculator
If you do not know your agno for the first semester find your letter grades and credits of your lessons for the first semester from your transcript and write your letter grades on 'givenLetterCredits' as letter than write credits on 'credits_current_semester' section as float and do not fill null values.You have to execute main.py now python3 main.py on the console you will see nxkr,and sum of credits values.Now write nxkr on   "nxkrPast_semesters" as an array and sum of credits values on "credit_sums_of_past_semesters" as an array. On credits you will write second semesters credits in this case and 2nd semesters letter grades to 'givenLetterCredits' and 'credits_current_semester' you have to almost write current lesson credits and letter credits but past nxkr and past lesson credits must be empty for the first semester and you have to fill them after first semester finished.Here is an example for third semester 
 "credit_sums_of_past_semesters": [
            19.5,
            20
        ]
and 
 "nxkrPast_semesters": [
            64.0,
            35.25
        ]
Please do not change anything on main.py use it only to execute agno function and use config.json for all configurations and do not change anything on "N" array on config.json! And use grades to see if you are passed or failed from any lesson or to see how many grade you have to get by final exam to pass from a lesson giving your ssi and absence scores.If ssi and absence scores are lacked you will get an error message to pass these values on config.json.The file config.json will come with a default configuration feel free to change its values according to your credits and grades but please do not touch 'N' array.Thanks for using my application😊

# Configuration Example For Config.json
{
    "Credits": {
        "N": [
            {
                "AA": 4.0
            },
            {
                "BA": 3.5
            },
            {
                "BB": 3.0
            },
            {
                "CB": 2.5
            },
            {
                "CC": 2.0
            },
            {
                "FF": 0.0
            }
        ],
        "givenLetterCredits": [
            "FF",
            "CC",
            "CB",
            "BA",
            "CB",
            "FF",
            "BB",
            "CC",
            "FF"
        ],
        "credit_sums_of_past_semesters": [
            19.5
        ],
        "credits_current_semester": [
            2.5,
            2.5,
            2.5,
            2.5,
            1.5,
            2.5,
            2.5,
            2.0,
            2.5
        ],
        "nxkrPast_semesters": [
            64.0
        ]
    },
    "Grades": 
        {
            "ssi": 100,
            "absence": 100,
            "final": null
        }
}