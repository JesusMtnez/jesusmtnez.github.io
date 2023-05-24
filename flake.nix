{
  description = "JesusMtnez's blog";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    theme = {
      url = "github:luizdepra/hugo-coder";
      flake = false;
    };
  };

  outputs = { self, nixpkgs, flake-utils, theme }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        themeName = ((builtins.fromTOML (builtins.readFile "${theme}/theme.toml")).name);
      in
      {

        packages.website = pkgs.stdenv.mkDerivation rec {
          pname = "jesusmtnez-website";
          version = (builtins.substring 0 8 self.lastModifiedDate);
          src = ./.;
          nativeBuildInputs = [ pkgs.hugo ];
          configurePhase = ''
            mkdir -p "themes/${themeName}"
            cp -r ${theme}/* "themes/${themeName}"
          '';
          buildPhase = "hugo --destination $out";
          dontInstal = true;
        };

        defaultPackage = self.packages.${system}.website;

        devShell = pkgs.mkShell {
          name = "website-shell";
          packages = [ pkgs.hugo ];
          shellHook = ''
            mkdir -p "themes"
            [[ ! -d themes/${themeName} ]] && ln -sn ${theme}/* "themes/${themeName}"
          '';
        };
      }
    );
}
