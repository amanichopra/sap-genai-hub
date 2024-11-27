# Building an Dash Application Consuming the Generative AI Hub

## Steps

1. Install dependency packages via `pip install dash dash-bootstrap-components`. 
2. Fill in the `get_summary_using_gen_ai_hub()` function in `app.py`. Your code should look something like below.
3. Run the app via `python app.py`.

```
config = OrchestrationConfig(
    llm=LLM(name=llm),
    template=Template(
        messages=[
            SystemMessage("You are a helpful chatbot assistant whose job is to summarize text."),
            UserMessage("{{?user_query}}"),
        ],
    ),
)

orchestration_service = OrchestrationService(
api_url=os.environ["AICORE_ORCHESTRATION_DEPLOYMENT_URL"],
config=config,
) 

response = orchestration_service.run(
        template_values=[
            TemplateValue(name="user_query", value=text),
        ]
    )

summary = response.orchestration_result.choices[0].message.content
```