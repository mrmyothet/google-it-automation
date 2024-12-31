### Terms and definitions (Automating Real-World Tasks with Python)

- **Distributed systems:** Also referred to as distributed computing or distributed databases, utilize different nodes to interact and synchronize over a shared network
- **Docstrings:** Documentation that lives alongside the code
- **NALSD (Non-Abstract Large System Design):** A discipline and process introduced by Google, primarily aimed at empowering site reliability engineers (SREs) to assess, design, and evaluate large-scale systems
- **Naming conventions:** Functions, classes and methods with naming conventions to understand what to expect from them

---

**Python Imaging Library** (known as **Pillow** in newer versions) is a library in Python that adds support for opening, manipulating, and saving lots of different image file formats.

Pillow offers several standard procedures for image manipulation. These include:

- Per-pixel manipulations
- Masking and transparency handling
- Image filtering, such as blurring, contouring, smoothing, or edge finding
- Image enhancing, like sharpening and adjusting brightness, contrast or color
- Adding text to images (and much more!)

---

```bash

pip install pipenv

pipenv install pipenv

```

- [Developing RESTful APIs with Python and Flask](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
- [Creating a Serverless REST API with GCP](https://medium.com/mdblog/creating-a-serverless-rest-api-with-gcp-32cc62188a03)

---

### Constraints with the REST architecture

The six constraints or principles of REST each serve a specific purpose in guiding the design of RESTful systems, contributing to the overall scalability, simplicity, and interoperability of the architecture.

- **Uniform interface** - There should be consistent methods for clients to access and change resources on the server using standard HTTP (Hypertext Transfer Protocol) conventions.
- **Stateless** - Every piece of information the server requires to process the request should be within the request. There shouldn't be any leftover information on the server between requests.
- **Cacheable** - Every server response should indicate whether the data can be cached on the client and the length of time is needed to cache the data.
- **Client-server** - The client and server can evolve independently. The REST interface serves as a “contract” between them.
- **Layered system** - An application should be split into layers. Each layer of the application handles a particular concern (data access, business logic, presentation, etc) and acts independently from the other layers.
- **Code on demand (optional)** - Servers can also provide code to be executed on the client. This enables the client to change its behavior dynamically.

---

### Richardson Maturity Model?

The Richardson Maturity Model, also known as RMM, is a framework that categorizes and describes different levels of implementation for RESTful APIs based on their adherence to the six constraints referenced earlier in this reading. RMM is a way of assessing the sophistication of a REST API based on how compliant it is with the REST constraints.

The Richardson Maturity Model consists of four levels, each representing a progressive level of adherence to the principles of REST:

- **Level 0** - A single URI (uniform resource identifier) and a single verb (usually GET or POST)
- **Level 1** - Multiple URIs but still a single verb
- **Level 2** - Makes use of URIs and multiple methods, but is not HATEOAS (Hypermedia as the Engine of Application State)
- **Level 3** - Full HATEOAS

---

### Python tools for REST APIs

##### Client Side

- Requests
- HTTPX
- AIOHTTP
- PycURL
- [HTTPX vs Requests vs AIOHTTP](https://oxylabs.io/blog/httpx-vs-requests-vs-aiohttp)

##### Server Side

- Flask
- Django
- FastAPI
- [Top 10 Python REST API Frameworks in 2024](https://www.browserstack.com/guide/top-python-rest-api-frameworks)

### Flask

- [Quick Start](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)
- [15 Useful Flask Extensions and Libraries That I Use in Every Project](https://nickjanetakis.com/blog/15-useful-flask-extensions-and-libraries-that-i-use-in-every-project)
- [Official Tutorials](https://flask.palletsprojects.com/en/stable/tutorial/)
- [How to Build a Flask Python Web Application from Scratch](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)

---

### Data Serialization and Deserialization

| **Python**                                   | **JSON** |
| -------------------------------------------- | -------- |
| `dict`                                       | `object` |
| `list`, `tuple`                              | `array`  |
| `str`                                        | `string` |
| `int`, `float`, `int- & float-derived Enums` | `number` |
| `True`                                       | `true`   |
| `False`                                      | `false`  |
| `None`                                       | `null`   |
