## My MicroK8s Addons

This is my addons repository for MicroK8s. I will be creating addons that don't currently exist for configuring my MicroK8s cluster. The current template repository contains one addons:

  * opentelemetry-operator, an addon that installs the `opentelemetry-operator` helm chart.

### How to use this addons repository

#### Adding the repository
3rd party addons repositories are supported on MicroK8s v1.24 and onwards. To add a repository on an already installed MicroK8s you have to use the `microk8s addons repo` command and provide a user-friendly repo name, the path to the repository, and optionally a branch within the repository.

For example:

```
microk8s addons repo add phillipsj https://github.com/phillipsj/microk8s-addons --reference main
```

As long as you have a local copy of a repository and that repository is also a git one, it can also be added to a MicroK8s installation with:

```
microk8s.addons repo add phillipsj ./microk8s-addons
```

#### Enabling/disabling addons

The addons of all repositories are shown in `microk8s status` along with the repo they came from. `microk8s enable` and `microk8s disable` are used to enable and disable the addons respectively. The repo name can be used to disambiguate between addons with the same name. For example:

```
microk8s enable phillipsj/opentelemetry-operator
```

#### Refreshing the repository

Adding a repository to MicroK8s (via `mcirok8s addons repo add`) creates a copy of the repository under `$SNAP_COMMON/addons` (typically under `/var/snap/microk8s/common/addons/`). Authorized users are able to edit the addons to match their needs. In case the upstream repository changes and you need to pull in any updates with:

```
microk8s addons repo update phillipsj
```

#### Removing the repository

Removing repositories is done with:

```
microk8s addons repo remove phillipsj
```

## Adding new addons

See [`HACKING.md`](./HACKING.md) for instructions on how to develop custom MicroK8s addons.
