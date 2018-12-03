FROM ubuntu:18.04

MAINTAINER Sergei Zabolotskikh <sergei@adblockplus.org>

# We build V8 for arm but it requires to run mksnapshot of the same bitness on the host, thus we need to run 32 bit mksnapshot. However in order to do it one has to install libc6:i386 because currently the host runns only 64 bit applications.
# Add i386 arch in order to install libc6:i386.
RUN dpkg --add-architecture i386
RUN apt-get update -qyy

RUN apt-get install -qyy \
  sudo \
  dumb-init \
  curl \
  libc6:i386

RUN curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | bash

COPY pin-gitlab-runner.pref /etc/apt/preferences.d/pin-gitlab-runner.pref

RUN apt-get install -qyy \
  gitlab-runner

RUN adduser --gecos "" --disabled-password ci_user \
  && usermod -aG sudo ci_user \
  && echo "ci_user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN mkdir /opt/ci
RUN chown -R ci_user:ci_user /opt/ci

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["gitlab-runner", "run", "--working-directory", "/opt/ci", "--user", "ci_user"]
