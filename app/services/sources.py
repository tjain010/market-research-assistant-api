from urllib.parse import quote_plus


def generate_starter_sources(topic: str, research_type: str):
    encoded_topic = quote_plus(topic)

    if research_type == "company":
        return [
            {
                "label": "Official company website",
                "url": guess_company_url(topic)
            },
            {
                "label": "Company news search",
                "url": f"https://www.google.com/search?q={encoded_topic}+news"
            },
            {
                "label": "Competitor search",
                "url": f"https://www.google.com/search?q={encoded_topic}+competitors"
            },
            {
                "label": "Industry analysis search",
                "url": f"https://www.google.com/search?q={encoded_topic}+industry+analysis"
            }
        ]

    elif research_type == "market":
        return [
            {
                "label": "Market trends search",
                "url": f"https://www.google.com/search?q={encoded_topic}+market+trends"
            },
            {
                "label": "Leading companies search",
                "url": f"https://www.google.com/search?q={encoded_topic}+leading+companies"
            },
            {
                "label": "Industry reports search",
                "url": f"https://www.google.com/search?q={encoded_topic}+industry+report"
            },
            {
                "label": "Customer demand search",
                "url": f"https://www.google.com/search?q={encoded_topic}+customer+demand"
            }
        ]

    elif research_type == "comparison":
        return [
            {
                "label": "Comparison search",
                "url": f"https://www.google.com/search?q={encoded_topic}+comparison"
            },
            {
                "label": "Pricing comparison search",
                "url": f"https://www.google.com/search?q={encoded_topic}+pricing"
            },
            {
                "label": "Feature comparison search",
                "url": f"https://www.google.com/search?q={encoded_topic}+features"
            },
            {
                "label": "Documentation search",
                "url": f"https://www.google.com/search?q={encoded_topic}+documentation"
            }
        ]

    else:
        return [
            {
                "label": "Overview search",
                "url": f"https://www.google.com/search?q={encoded_topic}+overview"
            },
            {
                "label": "Major players search",
                "url": f"https://www.google.com/search?q={encoded_topic}+major+players"
            },
            {
                "label": "Trend search",
                "url": f"https://www.google.com/search?q={encoded_topic}+trends"
            },
            {
                "label": "Background reading search",
                "url": f"https://www.google.com/search?q={encoded_topic}+background"
            }
        ]


def guess_company_url(topic: str):
    lowered = topic.lower()

    known_companies = {
        "ibm": "https://www.ibm.com",
        "microsoft": "https://www.microsoft.com",
        "google": "https://www.google.com",
        "amazon": "https://www.amazon.com",
        "meta": "https://about.meta.com",
        "openai": "https://www.openai.com",
        "anthropic": "https://www.anthropic.com",
        "nvidia": "https://www.nvidia.com",
        "oracle": "https://www.oracle.com",
        "salesforce": "https://www.salesforce.com",
        "intel": "https://www.intel.com"
    }

    for company, url in known_companies.items():
        if company in lowered:
            return url

    encoded_topic = quote_plus(topic)
    return f"https://www.google.com/search?q={encoded_topic}+official+website"