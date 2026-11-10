---
Use this skill when I ask you to study, analyze, inspect, or understand an entire codebase before making any changes.
---

Your task is to build a thorough understanding of the entire codebase before performing any implementation work.

Inspect and understand all relevant parts of the project, including:

1. Every function, class, module, package, and service.
2. Infrastructure files, deployment files, container configurations, and cloud resources.
3. Workflows, background jobs, scheduled tasks, event driven processes, and automation.
4. Configuration files, environment variables, feature flags, and application settings.
5. The overall purpose and intent of the project.
6. The product or service being delivered to the client.
7. How the application starts, runs, and is deployed.
8. How endpoints are exposed and served.
9. The structure of request bodies, response bodies, headers, authentication, and error responses.
10. The responsibilities of each service and component.
11. How services communicate with each other.
12. Data flow between APIs, databases, queues, caches, external services, and background workers.
13. Database schemas, models, migrations, repositories, and persistence patterns.
14. Test cases, fixtures, mocks, integration tests, end to end tests, and expected behavior.
15. Coding conventions, architectural patterns, design patterns, and dependency boundaries.
16. Logging, monitoring, tracing, retry logic, timeout handling, and error handling.
17. Security, permissions, secrets management, and authentication flows.
18. Known assumptions, possible risks, unclear behavior, and areas that may require further investigation.

When the project uses a microservice architecture, identify every service and explain how the services connect, communicate, and depend on each other.

Trace important workflows from beginning to end. For example, follow a request from the client, through the API layer, business logic, database or external services, and finally to the returned response.

Do not modify, create, delete, format, or refactor any code.

Do not implement fixes or improvements, even if you notice problems.

Do not make assumptions when the code provides evidence. Base your understanding on the actual repository contents.

You may run safe, read only commands to inspect the repository, dependencies, configuration, tests, and project structure. Do not run commands that modify files, infrastructure, databases, or external systems.

After reviewing the codebase, provide a structured summary that covers:

1. The purpose of the project.
2. The main architecture.
3. The responsibilities of each major component.
4. The important workflows and data flows.
5. The API request and response structures.
6. The testing strategy.
7. The coding and design patterns being used.
8. The infrastructure and deployment approach.
9. Any unclear areas, risks, or missing context.
10. A concise mental model of how the entire system works.

For now, your only objective is to understand the project thoroughly and prepare for the task I will provide next.
