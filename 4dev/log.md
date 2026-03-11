WARN[0000] /Users/aleksandrsamohvalov/Documents/GitHub/selectest-api-way/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 3/3
 ✔ Container selectest-api-way-app-1  Removed                                                                                                                                    0.0s 
 ✔ Container selectest-api-way-db-1   Removed                                                                                                                                    0.0s 
 ✔ Network selectest-api-way_default  Removed                                                                                                                                    0.2s 
WARN[0000] /Users/aleksandrsamohvalov/Documents/GitHub/selectest-api-way/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Building 5.9s (12/12) FINISHED                                                                                                                                                    
 => [internal] load local bake definitions                                                                                                                                       0.0s
 => => reading from stdin 583B                                                                                                                                                   0.0s
 => [internal] load build definition from Dockerfile                                                                                                                             0.0s
 => => transferring dockerfile: 297B                                                                                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                              1.6s
 => [internal] load .dockerignore                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                  0.0s
 => [1/5] FROM docker.io/library/python:3.11-slim@sha256:d6e4d224f70f9e0172a06a3a2eba2f768eb146811a349278b38fff3a36463b47                                                        0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:d6e4d224f70f9e0172a06a3a2eba2f768eb146811a349278b38fff3a36463b47                                                        0.0s
 => [internal] load build context                                                                                                                                                0.2s
 => => transferring context: 1.33MB                                                                                                                                              0.2s
 => CACHED [2/5] WORKDIR /app                                                                                                                                                    0.0s
 => CACHED [3/5] COPY requirements.txt /app/                                                                                                                                     0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                                              0.0s
 => [5/5] COPY . /app/                                                                                                                                                           1.2s
 => exporting to image                                                                                                                                                           2.4s
 => => exporting layers                                                                                                                                                          1.8s
 => => exporting manifest sha256:ac8c1ed94b39b46ef3953e8a19859a9f7b4d3dc3adf3ce6994df82efe21ef515                                                                                0.0s
 => => exporting config sha256:34c666561887f204d8cb554dc6e628d023e0f2ba794dad03065fa829d82dd21f                                                                                  0.0s
 => => exporting attestation manifest sha256:b8bdd1a9f3b22d839bbf6c1c7f6eb37079d24fbfcde7f227f309c14e9d591cc3                                                                    0.0s
 => => exporting manifest list sha256:e42b50ec1ec266a42e58ec2cebc1267a0cd7528c129ae2fc4c28c25d127bc217                                                                           0.0s
 => => naming to docker.io/library/selectest-api-way-app:latest                                                                                                                  0.0s
 => => unpacking to docker.io/library/selectest-api-way-app:latest                                                                                                               0.6s
 => resolving provenance for metadata file                                                                                                                                       0.0s
[+] Running 4/4
 ✔ selectest-api-way-app              Built                                                                                                                                      0.0s 
 ✔ Network selectest-api-way_default  Created                                                                                                                                    0.0s 
 ✔ Container selectest-api-way-db-1   Created                                                                                                                                    0.3s 
 ✔ Container selectest-api-way-app-1  Created                                                                                                                                    0.0s 
Attaching to app-1, db-1
db-1  | 
db-1  | PostgreSQL Database directory appears to contain a database; Skipping initialization
db-1  | 
db-1  | 2026-03-11 12:26:51.507 UTC [1] LOG:  starting PostgreSQL 16.13 (Debian 16.13-1.pgdg13+1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
db-1  | 2026-03-11 12:26:51.507 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db-1  | 2026-03-11 12:26:51.507 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db-1  | 2026-03-11 12:26:51.509 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db-1  | 2026-03-11 12:26:51.511 UTC [29] LOG:  database system was shut down at 2026-03-11 12:26:41 UTC
db-1  | 2026-03-11 12:26:51.514 UTC [1] LOG:  database system is ready to accept connections
app-1  | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
app-1  | INFO  [alembic.runtime.migration] Will assume transactional DDL.
app-1  | INFO:     Started server process [1]
app-1  | INFO:     Waiting for application startup.
app-1  | 2026-03-11 12:26:58,373 | INFO | app.main | Запуск приложения
app-1  | 2026-03-11 12:26:58,373 | INFO | app.services.parser | Старт парсинга вакансий
app-1  | 2026-03-11 12:26:59,136 | INFO | httpx | HTTP Request: GET https://api.selectel.ru/proxy/public/employee/api/public/vacancies?per_page=1000&page=1 "HTTP/1.1 200 OK"
app-1  | 2026-03-11 12:26:59,202 | INFO | app.services.parser | Парсинг завершен, новых вакансий: 0
app-1  | 2026-03-11 12:26:59,205 | INFO | apscheduler.scheduler | Adding job tentatively -- it will be properly scheduled when the scheduler starts
app-1  | 2026-03-11 12:26:59,205 | INFO | apscheduler.scheduler | Added job "_run_parse_job" to job store "default"
app-1  | 2026-03-11 12:26:59,205 | INFO | apscheduler.scheduler | Scheduler started
app-1  | INFO:     Application startup complete.
app-1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
app-1  | INFO:     192.168.65.1:46885 - "GET /api/v1/vacancies/?timetable_mode_name=%D0%93%D0%B8%D0%B1%D0%BA%D0%B8%D0%B9&city=%D1%81%D0%B0%D0%BD%D0%BA%D1%82 HTTP/1.1" 200 OK
app-1  | INFO:     192.168.65.1:23985 - "POST /api/v1/vacancies/ HTTP/1.1" 201 Created
app-1  | INFO:     192.168.65.1:57555 - "GET /api/v1/vacancies/32 HTTP/1.1" 200 OK
app-1  | INFO:     192.168.65.1:54534 - "PUT /api/v1/vacancies/32 HTTP/1.1" 200 OK
app-1  | INFO:     192.168.65.1:63363 - "DELETE /api/v1/vacancies/32 HTTP/1.1" 204 No Content
app-1  | INFO:     192.168.65.1:48616 - "DELETE /api/v1/vacancies/33 HTTP/1.1" 404 Not Found
db-1   | 2026-03-11 12:31:51.601 UTC [27] LOG:  checkpoint starting: time
db-1   | 2026-03-11 12:31:52.045 UTC [27] LOG:  checkpoint complete: wrote 7 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.431 s, sync=0.004 s, total=0.445 s; sync files=6, longest=0.003 s, average=0.001 s; distance=8 kB, estimate=8 kB; lsn=0/1570500, redo lsn=0/15704C8
app-1  | 2026-03-11 12:31:59,212 | INFO | apscheduler.executors.default | Running job "_run_parse_job (trigger: interval[0:05:00], next run at: 2026-03-11 12:36:59 UTC)" (scheduled at 2026-03-11 12:31:59.205106+00:00)
app-1  | 2026-03-11 12:31:59,217 | INFO | app.services.parser | Старт парсинга вакансий
app-1  | 2026-03-11 12:31:59,998 | INFO | httpx | HTTP Request: GET https://api.selectel.ru/proxy/public/employee/api/public/vacancies?per_page=1000&page=1 "HTTP/1.1 200 OK"
app-1  | 2026-03-11 12:32:00,057 | INFO | app.services.parser | Парсинг завершен, новых вакансий: 0
app-1  | 2026-03-11 12:32:00,058 | INFO | apscheduler.executors.default | Job "_run_parse_job (trigger: interval[0:05:00], next run at: 2026-03-11 12:36:59 UTC)" executed successfully
app-1  | 2026-03-11 12:36:59,211 | INFO | apscheduler.executors.default | Running job "_run_parse_job (trigger: interval[0:05:00], next run at: 2026-03-11 12:41:59 UTC)" (scheduled at 2026-03-11 12:36:59.205106+00:00)
app-1  | 2026-03-11 12:36:59,216 | INFO | app.services.parser | Старт парсинга вакансий
app-1  | 2026-03-11 12:36:59,992 | INFO | httpx | HTTP Request: GET https://api.selectel.ru/proxy/public/employee/api/public/vacancies?per_page=1000&page=1 "HTTP/1.1 200 OK"
app-1  | 2026-03-11 12:37:00,034 | INFO | app.services.parser | Парсинг завершен, новых вакансий: 0
app-1  | 2026-03-11 12:37:00,036 | INFO | apscheduler.executors.default | Job "_run_parse_job (trigger: interval[0:05:00], next run at: 2026-03-11 12:41:59 UTC)" executed successfully
