let

  sources = import ./nix/sources.nix;
  nixpkgs = sources.nixpkgs;
  niv = sources.niv;
  pkgs = import nixpkgs {};

  theme = sources.hugo-coder;
  hugo-coder = pkgs.runCommand "hugo-coder" {
    pinned = builtins.fetchTarball {
      name = theme.repo + "-" + theme.rev;
      url = theme.url;
      sha256 = theme.sha256;
    };

    patches = [];

    preferLocalBuild = true;
  }
  ''
    cp -r $pinned $out
    chmod -R u+w $out
  '';

in pkgs.mkShell rec {

  name = "blog";

  buildInputs = with pkgs; [
    (import niv { }).niv
    hugo
  ];

  shellHook = ''
    mkdir -p themes
    ln -snf "${hugo-coder}" themes/hugo-coder
    export NIX_PATH="nixpkgs=${nixpkgs}
  '';
}
