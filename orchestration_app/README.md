# Building an Dash Application Consuming the Generative AI Hub

Now that you've learned about the capabilities of Orchestration, let's build a Python app that consumes the service.

## Steps

1. Install dependency packages via `pip install dash dash-bootstrap-components`. 
2. Ensure there is a file called `env_vars.env` in the root project folder containing the credentials to access AI Core. If you completed the other exercises, you must have already performed this step.
3. Fill in the `get_summary_using_gen_ai_hub()` function in `app.py`. Your code should look something like below.
4. Run the app via `python app.py`.
5. You'll see a popup in the bottom right corner stating `A service is listening to port 8050.`. Click `Open in a New Tab`.

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
deployment_id=os.environ["AICORE_ORCH_DEPLOYMENT_ID"],
config=config,
) 

response = orchestration_service.run(
        template_values=[
            TemplateValue(name="user_query", value=text),
        ]
    )

summary = response.orchestration_result.choices[0].message.content
```