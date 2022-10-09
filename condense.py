import cohere
co = cohere.Client('kvVDmVLdLI3Oumt51Hj9p0h43vaeEUHZzTiL972O')


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
