import cohere
co = cohere.Client('{API_KEY}')


def condenser(text):
    response = co.generate(
        model='large',
        prompt=text,
        max_tokens=50,
        temperature=0.8,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        return_likelihoods='NONE')
    return(response.generations[0].text)
