FROM harbor.vantage6.ai/algorithms/algorithm-base
# Needs to be the same as name in the `setup.py`.
ARG PKG_NAME="v6-tidal-py"
COPY . /app
RUN pip install /app
ENV PKG_NAME=${PKG_NAME}
CMD python -c "from vantage6.tools.docker_wrapper import docker_wrapper; docker_wrapper('${PKG_NAME}')"