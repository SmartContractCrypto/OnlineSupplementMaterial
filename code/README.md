## Source code for the quantitative analysis

This directory contains the source code for the quantitative analysis presented in our paper. Please refer to the README file in the `./code` directory for details to run the code and reproduce the results.

1. Contracs.py: Source code for the quantitative analysis in Section 3.
2. StackExchangePosts.py: Source code for the quantitative analysis in Section 4.
3. SurveyResults.py: Source code for the quantitative analysis in Section 5.



## Reproduce the results

Python environment:  Tested with python 3.10

Python dependencies: Please use pip3 to install dependencies in `requirements.txt`.

````cmd
pip3 install -r requirements.txt
````

Then run these source code with python3. For example, to reproduce the quantitative analysis result in Section 4, run the following commands: 

```cmd
python3 StackExchangePosts.py
```

The expected output is: 

```
------------------------------------------------------------ Hash ------------------------------------------------------------
Number of Hash-related Posts: 243
Number of Obstacles in Hash-related Posts: {'N/A': 148, 'Knowledge': 11, 'Security': 10, 'Crypto API Usage': 51, 'Roadmap Identification': 20, 'Template Usage': 3}
Proportion of Obstacles in Hash-related Posts: {'Knowledge': '11.6%', 'Security': '10.5%', 'Crypto API Usage': '53.7%', 'Roadmap Identification': '21.1%', 'Template Usage': '3.2%'}
------------------------------------------------------------ Signature ---------------------------------------------------------
Number of Signature-related Posts: 200
Number of Obstacles in Signature-related Posts: {'N/A': 79, 'Template Usage': 39, 'Knowledge': 13, 'Security': 7, 'API Usage': 30, 'Roadmap Identification': 32}
Proportion of Obstacles in Signature-related Posts: {'Template Usage': '32.2%', 'Knowledge': '10.7%', 'Security': '5.8%', 'API Usage': '24.8%', 'Roadmap Identification': '26.4%'}
------------------------------------------------------------ ZKP ------------------------------------------------------------
Number of ZKP-related Posts: 40
Number of Obstacles in ZKP-related Posts: {'Roadmap Identification': 17, 'Knowledge': 7, 'Template Usage': 5, 'API Usage': 2, 'Security ': 3, 'N/A': 6}
Proportion of Obstacles in ZKP-related Posts: {'Roadmap Identification': '50.0%', 'Knowledge': '20.6%', 'Template Usage': '14.7%', 'API Usage': '5.9%', 'Security ': '8.8%'}
```

